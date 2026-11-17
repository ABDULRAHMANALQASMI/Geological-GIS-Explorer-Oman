# Known limitations / pre-publication caveats

- **Not exhaustive:** 27 publicly sourced geological unit/complex summaries are a research starting set, not every formation in Oman.
- **Published concession boundary image:** A ministry-attributed map printed in December 2025 is displayed from the OPAL source. It is not a machine-readable licensed polygon layer; a future vector layer needs authoritative geometry. Older operator rosters are labelled historical.
- **No authenticated live operational data:** LAS input and calculations are for local teaching / analysis, not a drilling safety decision.
- **No GeoTIFF rendering or arbitrary CRS transformations in the browser:** Convert separately before import.
- **Partial bilingual UI:** Navigation items and key labels are translated; all advanced scientific descriptions are currently English. Full Arabic proofreading and RTL localization remain open tasks.
- **No React/TypeScript build in this release:** The existing polished frontend is a working dependency-light HTML/CSS/JS app; migration to React and TypeScript is a future refactor, not a falsely claimed completion.
- **No PostGIS database deployed:** SQL schema exists for an optional future deployment. FastAPI endpoints use local JSON and per-request computations.
- **Scientific geology figure under CC BY 4.0:** Scharf et al. (2021) Fig. A.1 is included as an optimized image with full author citation and license link. Other publisher figures should be separately checked.
- **Internet dependencies:** Leaflet, Turf, KML/Shapefile parsers, OSM and Esri map tiles depend on third-party CDNs/endpoints. Tile provider policies and availability must be confirmed before high-traffic deployment.
- **Read-only API:** No authentication, storage or enterprise workflows, and not designed for private client data or secure operational ingestion.
- **No current accuracy guarantee:** Research check as of 2026-11-17. Publicly disclosed block participation may lag ministry licensing changes.
