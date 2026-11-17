# V4 verification report — 17 November 2026

## Verified in this execution
- `node --check app.js` — JavaScript parses successfully.
- `node --test tests/verify.mjs` — dataset, source, scientific map rights, publication dates, page copy, branding, V4 bibliographic integrity and spatial provenance checks. See actual console results.
- `python -m pytest -q tests/test_api.py` — optional FastAPI geometry, calculations and validation tests (if environment dependencies available).
- JSON validation of all scientific data and source references; new mapped units include a 2021 open scientific source ID.
- ZIP generated with SHA-256 checksums and verified CRC entries.

## Not executed / runtime blocker
Browser automation with system Chromium was attempted; the sandbox browser returned `ERR_BLOCKED_BY_ADMINISTRATOR` for both localhost HTTP and `file://` loads. Therefore this release **has not received a passing V4 visual-browser or touch-device inspection in this execution**.

## Requires testing on user machine before public release
- Source-hosted OPAL 2025 map image hotlinking and zoom on Chrome/Safari. The external source may change or prevent embedding. The page provides direct-source links as fallback.
- Public Leaflet map tiles and GIS converters (CDN).
- Mobile responsive behavior and full keyboard/screen-reader audit.
- All external source URLs and company/operator statuses as of publication date.
- LAS and Shapefile files at production size, as well as WMS services.
- Licensing or permission for redistribution of any additional third-party geological figure.

## Release note
This is an enhanced research-site deliverable, not a substitute for licensed official vector concession shapefiles. The 2025 external map is documented cartography, **not** a vector overlay that supports per-block polygon intersection.
