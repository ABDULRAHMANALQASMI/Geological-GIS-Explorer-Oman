from fastapi.testclient import TestClient
from backend.main import app
c=TestClient(app)

def test_health():
    x=c.get('/api/health');assert x.status_code==200;assert x.json()['official_concession_polygons_bundled'] is False

def test_catalog():
    x=c.get('/api/catalog/formations?q=Natih').json();assert x['count']>=1 and any(r['name']=='Natih' for r in x['items'])

def test_geodesic_polygon():
    ft={'type':'Polygon','coordinates':[[[57,22],[57.05,22],[57.05,22.05],[57,22.05],[57,22]]]}
    x=c.post('/api/spatial/measure',json={'geojson':ft});assert x.status_code==200
    assert 25<x.json()['results'][0]['area_km2']<35

def test_intersection():
    a={'type':'Polygon','coordinates':[[[57,22],[58,22],[58,23],[57,23],[57,22]]]}
    b={'type':'Polygon','coordinates':[[[57.5,22.5],[58.2,22.5],[58.2,23.2],[57.5,23.2],[57.5,22.5]]]}
    x=c.post('/api/spatial/intersect',json={'a':a,'b':b}); assert x.status_code==200
    assert x.json()['intersects'] and x.json()['metrics']['area_km2']>0

def test_invalid_longitude():
    x=c.post('/api/spatial/measure',json={'geojson':{'type':'Point','coordinates':[194,22]}});assert x.status_code==422

def test_lag_volume():
    args={'hole_in':8.5,'pipe_od_in':5,'length_m':1800,'flow_lpm':2200,'mud_weight_ppg':10,'tvd_ft':6000}
    x=c.post('/api/drilling/calculate',json=args);assert x.status_code==200;v=x.json();assert abs(v['hydrostatic_psi']-3120)<1e-6;assert v['annular_volume_m3']>0

def test_invalid_diameters():
    x=c.post('/api/drilling/calculate',json={'hole_in':5,'pipe_od_in':8.5,'length_m':100,'flow_lpm':1000});assert x.status_code==422
