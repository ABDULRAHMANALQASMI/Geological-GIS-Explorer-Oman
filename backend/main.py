"""GEO//OMAN public research API.

All data are public-source research summaries. Geometry uploads are held in memory
per request and never persisted. Geodesic metrics use WGS84 ellipsoid.
"""
from __future__ import annotations
import json, math, os
from pathlib import Path
from typing import Any
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from pyproj import Geod
from shapely.geometry import shape, mapping
from shapely.validation import explain_validity

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
GEOD = Geod(ellps='WGS84')
MAX_FEATURES = 2500
MAX_BODY_BYTES = 3_000_000
app = FastAPI(title='Geological GIS Explorer Oman', version='3.0.0',
    description='Publicly sourced geology catalog, dated concessions, spatial research computations')
origins = [s.strip() for s in os.getenv('GIS_CORS_ORIGINS', 'http://localhost:8000,http://127.0.0.1:8000,http://localhost:5173').split(',') if s.strip()]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=['GET','POST'], allow_headers=['Content-Type'])

@app.middleware('http')
async def body_limit(request: Request, call_next):
    if request.method in ('POST','PUT','PATCH'):
        length = request.headers.get('content-length')
        if length and int(length) > MAX_BODY_BYTES:
            return JSONResponse(status_code=413, content={'detail':'Upload too large'})
    return await call_next(request)

def dataset(name: str):
    if name not in {'formations','groups','statistics','sources','concessions','operators','events','regions','ophiolite'}:
        raise HTTPException(404,'Unknown dataset')
    return json.loads((DATA / f'{name}.json').read_text(encoding='utf-8'))

@app.get('/api/health')
def health():
    return {'status':'ok','version':'3.0.0','research_date':'2026-11-17','official_concession_polygons_bundled':False}

@app.get('/api/catalog/{name}')
def get_catalog(name: str, q: str = Query('',max_length=160), limit: int = Query(250, ge=1,le=500)):
    items=dataset(name)
    if q.strip():
        search=q.casefold().strip()
        items=[x for x in items if search in ' '.join(str(v) for v in x.values()).casefold()]
    return {'dataset':name,'count':len(items),'items':items[:limit], 'filtered':bool(q)}

class GeometryBody(BaseModel):
    geojson: dict[str,Any]

class IntersectBody(BaseModel):
    a: dict[str,Any]
    b: dict[str,Any]

class DrillingBody(BaseModel):
    hole_in: float = Field(gt=0, le=60)
    pipe_od_in: float = Field(ge=0, le=60)
    length_m: float = Field(gt=0, le=15000)
    flow_lpm: float = Field(gt=0, le=100000)
    mud_weight_ppg: float | None = Field(default=None, gt=0,le=30)
    tvd_ft: float | None = Field(default=None, ge=0,le=50000)


def feature_list(data: dict):
    typ = data.get('type')
    if typ == 'FeatureCollection': features = data.get('features')
    elif typ == 'Feature': features = [data]
    elif typ in {'Point','MultiPoint','LineString','MultiLineString','Polygon','MultiPolygon','GeometryCollection'}:
        features = [{'type':'Feature','geometry':data,'properties':{}}]
    else:raise HTTPException(422,'Expected GeoJSON Feature, FeatureCollection or geometry')
    if not isinstance(features,list) or len(features)>MAX_FEATURES:
        raise HTTPException(422,'Invalid feature array or too many features')
    return features

def coordinates(geom):
    if isinstance(geom,dict):
        for k,v in geom.items():
            if k=='coordinates':yield from coordinates(v)
            elif k=='geometries':yield from coordinates(v)
            elif isinstance(v,(dict,list)):yield from coordinates(v)
    elif isinstance(geom,list):
        if len(geom)>=2 and all(isinstance(q,(float,int)) for q in geom[:2]):
            yield geom
        else:
            for item in geom:yield from coordinates(item)

def to_geom(raw):
    item=raw.get('geometry',raw) if isinstance(raw,dict) else None
    if not item or not isinstance(item,dict):raise HTTPException(422,'Missing geometry')
    coords=list(coordinates(item))
    if len(coords)>75000:raise HTTPException(422,'Too many vertices')
    if any(not math.isfinite(a[0]) or not math.isfinite(a[1]) or abs(a[0])>180 or abs(a[1])>90 for a in coords):
        raise HTTPException(422,'Coordinates must be WGS84 decimal-degree lon/lat; CRS reprojection required before upload')
    try:g=shape(item)
    except Exception as ex:raise HTTPException(422,'Malformed geometry: '+str(ex)) from ex
    if g.is_empty:raise HTTPException(422,'Empty geometry')
    if not g.is_valid:raise HTTPException(422,'Invalid topology: '+explain_validity(g))
    return g

def metrics(g):
    area,perimeter=GEOD.geometry_area_perimeter(g)
    if g.geom_type in ('LineString','MultiLineString'):
        perimeter=GEOD.geometry_length(g)
    if g.geom_type in ('Point','MultiPoint'):
        perimeter=0
    return {'geometry_type':g.geom_type,'area_km2':round(abs(area)/1_000_000,6),
            'geodesic_length_km':round(abs(perimeter)/1000,6),
            'bounds_lonlat':list(map(float,g.bounds))}

@app.post('/api/spatial/measure')
def measure(body: GeometryBody):
    geoms=[to_geom(ft) for ft in feature_list(body.geojson)]
    return {'method':'WGS84 geodesic; pyproj.Geod; polygon perimeter or line length',
            'coordinate_reference_system':'EPSG:4326','count':len(geoms),
            'results':[metrics(g) for g in geoms]}

@app.post('/api/spatial/intersect')
def intersect(body:IntersectBody):
    a,b=to_geom(body.a),to_geom(body.b)
    intersection=a.intersection(b) # topology in lonlat: local polygons only; geodesic metrics below
    return {'intersects':not intersection.is_empty,'geometry':mapping(intersection) if not intersection.is_empty else None,
            'metrics':metrics(intersection) if not intersection.is_empty else None,
            'caveat':'WGS84 topology; avoid antimeridian-crossing or polar geometries; geodesic WGS84 area/length'}

@app.post('/api/drilling/calculate')
def drilling(body:DrillingBody):
    if body.hole_in<=body.pipe_od_in: raise HTTPException(422,'Hole diameter must exceed pipe outer diameter')
    annular_area=math.pi/4*((body.hole_in*.0254)**2-(body.pipe_od_in*.0254)**2)
    volume=annular_area*body.length_m
    lag_min=volume*1000/body.flow_lpm
    result={'annular_capacity_l_per_m':round(annular_area*1000,5), 'annular_volume_m3':round(volume,5),
            'theoretical_lag_minutes':round(lag_min,5), 'assumptions':'Ideal geometry and constant flow; calibrated real lag may differ'}
    if body.mud_weight_ppg is not None and body.tvd_ft is not None:
        psi=.052*body.mud_weight_ppg*body.tvd_ft
        result['hydrostatic_psi']=round(psi,4)
        result['hydrostatic_bar']=round(psi*.0689475729,4)
    return result
