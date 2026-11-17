# GEO//OMAN — Geological GIS Explorer V4.0

**Evidence-linked geological research and GIS workbench for the Sultanate of Oman.**

**Project creator:** عبد الرحمن القاسمي — **Abdulrahman Al Qasmi** · [Portfolio](https://abdulrahmanalqasmi.github.io/abdulrahman-portfolio/)

> RESEARCH BUILD — not an authoritative licensed geological survey, live concession register, field database, drilling management system or substitute for operational well-control procedures. All public records are date-stamped. The application never guesses concession polygons.

## Start in VS Code (Mac / Windows)

1. Unzip the project and use **File → Open Folder** in Visual Studio Code.
2. Select **Terminal → New Terminal**.
3. Run the no-install static frontend:

```sh
python3 -m http.server 8000
```

4. Open **http://localhost:8000**. On Windows `py -m http.server 8000` may be appropriate.
5. To stop, press `Control+C` in the terminal.

**The map tile layers and Javascript map libraries require internet access.** Open the site with HTTP, not a `file://` path. All geological catalog JSON files and original CSS/JS code are local and editable.

### Optional geospatial Python API

In a **second VS Code terminal**, from the project root:

```sh
python3 -m venv .venv
source .venv/bin/activate                     # Windows: .venv\Scripts\activate
pip install -r backend/requirements.txt
uvicorn backend.main:app --host 127.0.0.1 --port 8001 --reload
```

- API health: http://127.0.0.1:8001/api/health
- Swagger docs: http://127.0.0.1:8001/docs
- JSON catalog: http://127.0.0.1:8001/api/catalog/formations?q=Natih
- Geometry endpoints: `POST /api/spatial/measure`, `POST /api/spatial/intersect`; input must be WGS84 GeoJSON.
- Drilling math: `POST /api/drilling/calculate`.

The frontend works standalone. **The optional API is currently separate from the browser's calculations** to keep GitHub Pages deployment simple. For production backend integration, deploy API to a secure hosting platform and configure allowed origins.

## Scientific and functional coverage

| Area | Delivered in V4 |
|---|---|
| Scientific research | 29 referenced public sources including MEM, NCSI, USGS and peer-reviewed papers, each with access and usage notes |
| Stratigraphy | 59 public-literature indexed units within 18 geological groups/complex headings; 7+ core formation metadata fields |
| Geologic time | 6 evidence-linked periods/events with clickable research details |
| Oman mountains | 5 public research region dossiers; no invented exact site boundaries |
| Ophiolite | 8 clickable layers of an **idealized**, clearly labeled section |
| Oil and gas | 2025 output and resources distinctions, 2026 bid round, older official block records |
| Concessions | 44 **historical/announcement** records; published 2025 government boundary map image with date and source; no pseudo GIS polygons |
| Companies | Public older MEM concession entries plus 12 OQEP-reported partnership-interest snapshots; conflicts flagged |
| Spatial GIS | Live OSM/Esri basemaps (online), public-domain coarse Oman outline; upload GeoJSON, KML, CSV, ZIP Shapefile; geodesic area/length via Turf.js |
| Spatial analysis | Map measurements, polygon intersection for uploaded layers; optional WGS84 geodesic backend |
| Drilling | Annulus volume, idealized lag, hydrostatic pressure, pump strokes, local LAS curve preview |
| Data confidence | Source references, date, record type, disclosure stage, published source-hosted boundary map (2025), no inferred polygon data |
| Branding | Footer copyright and Visit My Portfolio button |

## Source and evidence details

All data are in [`data/`](data/) with the primary bibliography in [`data/sources.json`](data/sources.json) and its tabular export in [`docs/SOURCES.csv`](docs/SOURCES.csv).

**2025:** NCSI reports 365.8 million barrels of crude oil **including condensate**, preliminary. MEM reports average production 1,002.1 thousand barrels/day, 4,728 million barrel reserves and 151.2 million m³/day natural gas, as published in its portal. These are **different measures**. USGS published a *2023 assessment* in 2025 of approximately 1.2 billion barrels and 6.4 Tcf **undiscovered technically recoverable conventional resources**: this is neither current production nor proved reserves.

**Concessions:** The 12 April 2026 announcement offered Blocks 12, 16, 55, 42 and 45 for bidding. It is **not proof** of a later award. The Ministry's legacy directory has different operators/areas for some blocks. These are displayed separately and should not be merged into a current roster. The 2026 bid round closed for registration September 30, 2026 according to that announcement, so the site labels this a **historical 2026 bid round**, not an available opportunity today. Block 42 illustrates how older company disclosures can conflict with a subsequent tender; such entries are explicitly flagged.

**GIS:** `data/oman-boundary.geojson` is a coarse Natural Earth national context feature, **not** a map of geological units or hydrocarbon concessions. The [USGS 2025 assessment-unit spatial data](https://doi.org/10.5066/P1VRJXRI) may be downloaded separately; these units are petroleum-system assessment zones, **not licence block geometry**. The USGS data ZIP was not bundled; source download is provided for user review and ingestion.

**Quality notice:** Some formation ages, hierarchy and correlations vary regionally or between publications. Units are not well-specific tops and must be independently checked for any geological interpretation. Source link inclusion does not mean permission to reproduce photographs/figures.

## Data inputs

- **GeoJSON:** geographic coordinates WGS84 lon/lat in EPSG:4326.
- **CSV:** headers `lat`/`latitude` and `lon`/`longitude` with decimal degrees.
- **KML:** browser converter; geographic coordinate requirements apply.
- **Shapefile:** upload zipped `.shp`, `.shx`, `.dbf`, `.prj` sharing base name; confirm converted coordinates are WGS84. **The browser does not reproject arbitrary CRSs**.
- **LAS 2.0 ASCII:** local-only viewer, max 12MB and first 60,000 numeric lines; simple depth-versus-curve preview. No well log data leaves the browser.

For difficult data reprojection use desktop QGIS, GDAL, GeoPandas or the appropriate spatial API process before upload. GeoTIFF import is planned but **not yet implemented**.

## Data provenance and publish permissions

Read [`docs/SCIENTIFIC_METHOD.md`](docs/SCIENTIFIC_METHOD.md), [`docs/LIMITATIONS.md`](docs/LIMITATIONS.md), [`docs/TEST_REPORT.md`](docs/TEST_REPORT.md), and [`docs/ROADMAP.md`](docs/ROADMAP.md).

All supplied data summarize **independently published, public-domain, official or peer-reviewed sources**. No private drilling data, restricted internal logs or protected figures are in this delivery. External public information remains owned by its respective publishers. The project's original text, interface and code are attributed to Abdulrahman Al Qasmi.

## Test commands

```sh
node --check app.js
node --test tests/verify.mjs
# with optional backend environment installed:
python -m pytest -q tests/test_api.py
```

The browser user-interface testing was run in an isolated rendering environment; internet basemap loading and production third-party CDN availability could not be verified there. This is described in the test report.

## Deploy on GitHub Pages

The static app is directly deployable: push the **contents** of this directory (including `index.html`, `styles.css`, `app.js`, `data/`) and in **Settings → Pages** choose `Deploy from a branch`, branch `main`, root folder `/`. API routes and PostGIS need separate hosting; GitHub Pages serves static files only. See [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md).

## Folder layout

```text
Geological-GIS-Explorer-V4/
├── index.html                  public web app
├── styles.css                  responsive original visual system
├── app.js                      interactive atlas / GIS / LAS / calculators
├── data/                       public reference JSON and country outline
├── backend/main.py             optional FastAPI spatial research API
├── backend/requirements.txt
├── db/schema.sql               optional PostGIS schema (not instantiated)
├── docs/                       research, rights, verification, deployment
├── tests/                      JS catalog validation + Python API tests
└── .github/workflows/          automated static validations
```

© 2026 **Abdulrahman Al Qasmi — عبد الرحمن القاسمي**. Rights reserved for original contributions. Research references, imagery and external cartographic products retain their own rights and licences.


## V4 — Published concession map and expanded stratigraphy

- **Published concession boundaries:** viewer displays an external image hosted by OPAL of the Ministry map printed 24 December 2025; a separate linked PDF is dated 21 September 2021. This is a geographical cartographic reference and must not be equated with the 2026 tender roster or current operator ownership. The project does **not** bundle or invent georeferenced concession polygons. In offline settings, choose “OPEN ORIGINAL PDF” on a connected computer.
- **Open-access geology map:** Figure A.1 from Scharf et al. (2021), DOI `10.1144/M54.7`, CC BY 4.0, added as an optimized WebP with full credit.
- **Stratigraphy expansion:** additional figure-legend units with ages and `scharf2021map` provenance. Lithology and thickness are not fabricated when the source legend does not specify them.
- This atlas is for research and learning; operational drilling decisions require appropriate primary measurements and company-approved procedures.

## Updated published map image
2025 published concession map (printed 24 December 2025), hosted by OPAL Oman: https://opaloman.om/web/image/66528-79402fc1/MAP.png. The image is loaded directly from OPAL via URL; no local PNG copy is bundled. Map is historical relative to 2026 tender publication, and must not be presented as a live 2026 licensing map.

## GitHub publishing

For an Arabic step-by-step upload guide, see [`PUBLISH_ON_GITHUB_AR.md`](PUBLISH_ON_GITHUB_AR.md). The repository root contains `index.html` and `.nojekyll` for GitHub Pages static branch publishing.
