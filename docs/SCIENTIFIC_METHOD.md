# Scientific methodology and evidence standard · GEO//OMAN V3

**Review checkpoint: 17 November 2026**

## Dataset provenance policy

1. Prefer a first-party government statistical or licensing source for official reporting.
2. Prefer peer-reviewed science for tectonics, age, lithostratigraphy and source/reservoir interpretation.
3. Do not infer the exact geometry, well location, unit thickness, observed gas percentages or fracture azimuth from a narrative source.
4. Preserve historical dates and publication dates. Separate time-of-assessment, time-of-publication, and time-of-inspection.
5. Record data-source IDs on each scientific record. Only independently published information is incorporated; descriptions are new summaries.
6. Source figures and photos are linked at their original publisher's page rather than embedded or redrawn without permission.
7. Mark contested/reinterpretive tectonic models as interpretation, not unique established historical events.

## Scientific source map

- **Huqf/Neoproterozoic:** 2007 Huqf Supergroup basin paper; 2020 Nafun Group study.
- **Haima and early Paleozoic:** public GeoArabia sandstone/diagenesis paper, stratigraphic lexicon (secondary).
- **Haushi Late Paleozoic:** Cambridge peer-reviewed study of glaciogenic Al Khlata and postglacial Gharif deposits.
- **Jurassic Sahtan:** peer-reviewed Dhruma facies and 2017 integrated Triassic–Jurassic stratigraphic study.
- **Cretaceous:** published Natih chemostratigraphy/intrashelf-basin work and Rayda–Shuaiba carbonate-platform studies.
- **Ophiolite/mountain building:** 2025 *Tectonics* review of geochronology, 2020 *JGR* margin study, 2021 Geological Society Memoir and 2026 restored cross-sections.
- **Oil and gas resources:** USGS 2023 assessment published 2025; distinguishes assessment-unit geography from concession blocks.
- **Production/industry:** 2026 NCSI yearbook covering 2025 and MEM's 2025 performance summary, plus April 2026 bid round.

## Data confidence tiers

- `literature-supported`: general description directly supported by listed source(s); not proof of a specific well top.
- `regional-background`: included mainly to illustrate regional succession, further detailed sources needed.
- `age-varies-by-scheme` and `group-placement-varies`: a taxonomic or age attribution is not uniformly used across published literature.
- `dated-official`: the source documents a statement at a specified date; not evidence of current status after that date.
- `historical-only`: public historical ministry/company index; may conflict with more recent notices.
- `Not available as verified GIS polygon`: do not map an acreage boundary or imply geometry is accurate.

## Spatial semantics and CRS

- Country outline: Natural Earth 1:110m public domain, illustrative broad national context.
- User-uploaded EPSG:4326 GeoJSON layers: geographic WGS84 longitude and latitude. Do **not** treat geographic degrees as metres.
- Browser Turf.js area/length and Python pyproj.Geod metrics use geodesic computations; intersection topology uses longitude–latitude planar geometry and is suitable only for small regional extents avoiding dateline and polar edge cases.
- Official concession geometry: **none included**. No data should be implied just because a block number is known.
- USGS assessment-unit polygons: genuine research dataset is linked from USGS; user must download to ingest, and it must be displayed using the correct label **Assessment Unit**, not Concession.

## Protected and personal data

The public project deliberately excludes nonpublic well coordinates, operational gas logs, drilling schedules, proprietary reservoir mapping, protected PDF pages and unidentified imagery. Local imports stay in the browser. Backend endpoints process data per request without a database connection or persistence.

## Known scientific gaps

- Full national lithostratigraphic hierarchy and 3D correlation cannot be asserted without a broad, fully licensed source review.
- Exact formation thickness, fossils, chrono boundaries and petroleum roles are often local: missing properties are left absent rather than invented.
- Coastal/oceanic crustal sequences and dome metamorphic ages are active scientific interpretations.
- Operator shareholdings and block status may change between publication and present-day access.
- Approved mineral concession layers, geologic polygons, fault traces, DEM rasters, hillshade, GeoTIFFs and LAS calibrations require additional sourcing and validation.

Refer to `data/sources.json` and `docs/SOURCES.csv` for individual URL and publication metadata.
