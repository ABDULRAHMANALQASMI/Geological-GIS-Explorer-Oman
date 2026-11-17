# Geoscientific GIS production roadmap

## Next: verified geospatial data ingestion

- Download USGS data release DOI `10.5066/P1VRJXRI`, inspect full metadata, load assessment-unit geometry as **USGS AU**, not concession, and provide feature-specific citation.
- Obtain licensed geological polygons and fault traces from a public survey/provider; validate map scale, topology and CRS; generate reproducible import scripts.
- Obtain ministry-issued block geometry with a publication/effective date and operator status. Flag operator transitions and compare to public company disclosures.
- Add validated DEM / GeoTIFF raster rendering and WMS/WFS with service health checks and clear provider terms.

## Then: deeper geoscience

- Expand formation dossiers by individual peer-reviewed references with depositional cycles, unconformities, petrography, local thickness ranges and formal type sections where public.
- Distinguish lithostratigraphy, chronostratigraphy, biostratigraphy and sequence stratigraphy in separate correlated schemas.
- Add reusable Vail-style sequence visualization with clear **conceptual only** labelling unless measured sections supplied.
- Build lithology colour/texture/abbreviation standards and bounded local comparisons.
- Add licensed stratigraphic cross sections and borehole log displays, with source and license visible.

## Platform engineering

- Migrate to React/TypeScript with Vite, component/storybook test suite, automated visual regression, semantic i18n/RTL, robust file streaming.
- Connect FastAPI to PostgreSQL/PostGIS with migrations, API authentication, object storage and safe import jobs.
- Add tiling, chunked GeoJSON or vector tiles, caching, datasets registry, access control and admin publication workflow.
- Extend LAS support with `~Well`, curves/units, NULL, ASCII variants, depth direction, metadata and missing data handling; add unit tests for multiple real public formats.
- Add accessible map data tables, keyboard alternatives and performance profiling.

## Release gates

No claim of current concession operator/geographic boundary or scientific detail unless official and time-stamped; no protected figures/data; independent verification of imported GIS layers; responsive and accessibility audit; full browser test with real network; documented source refresh interval.
