# Deployment — GEO//OMAN V4

## Static frontend via GitHub Pages

1. Create a dedicated GitHub repository, ideally `Geological-GIS-Explorer`.
2. Add the project root files: `index.html`, `styles.css`, `app.js`, `data/`.
3. Push to `main`. In GitHub `Settings → Pages`, choose `Deploy from a branch` → `main` → `/(root)`.
4. Test the published URL including data loads and GIS base tiles.
5. Retain credits and linked source metadata, and verify third-party tile policies before public marketing.

This static architecture works without Node or npm. It is appropriate for GitHub Pages. Browser GIS libraries are currently loaded from CDNs and require network access.

## Optional Python API deployment

- Deploy `backend.main:app` to a Python host supporting Uvicorn, HTTPS, logs and environment variables.
- Run behind HTTPS reverse proxy, set production `GIS_CORS_ORIGINS` to the exact frontend origin (no `*`), and add network request body limits beyond the basic application-level guard.
- The API currently is **not automatically used by the static frontend**; it is an optional documented research service at `/api/*`.
- Do not expose internal/private field data or operation logs in public object storage.
- PostgreSQL/PostGIS schema in `db/schema.sql` is optional and must be migrated, configured and tested separately; do not commit DB credentials.

## Rights and maintenance

- User-owned original project work: Abdulrahman Al Qasmi.
- External scientific papers, satellite imagery, map tiles, and datasets: respective publishers' copyright and licences apply. Do not mirror their copyrighted figures without prior permission.
- Set a quarterly manual audit of MEM operator and concession announcements; note changes in records and their historical effective date.
- Test CDN and third-party map availability against the target deployment host.

## External map imagery (V4)
The concession map image is loaded from OPAL Oman at runtime (24 December 2025 print date); it is not copied into the repository. If remote hosting disallows embedding, use OPEN MAP IMAGE or the OPAL source link. Map availability and hotlinking must be checked after publishing. The local geology map image is CC BY 4.0 with attribution and original research link.
