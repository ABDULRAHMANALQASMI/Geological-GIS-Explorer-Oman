-- Optional PostGIS schema for deployment on managed PostgreSQL.
-- Run after CREATE EXTENSION postgis; no automatic migrations in static GitHub Pages.
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE TABLE IF NOT EXISTS research_sources (
 id TEXT PRIMARY KEY, title TEXT NOT NULL, author TEXT, published_on TEXT,
 doi TEXT, url TEXT, license TEXT, verified_on DATE, evidence_tier TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS geological_units (
 id TEXT PRIMARY KEY, name TEXT NOT NULL, stratigraphic_group TEXT,
 rank TEXT, geological_age TEXT, lithology TEXT, depositional_environment TEXT,
 summary TEXT, confidence TEXT, source_id TEXT REFERENCES research_sources(id)
);
CREATE TABLE IF NOT EXISTS concessions (
 id BIGSERIAL PRIMARY KEY, block_number TEXT NOT NULL, operator_name TEXT,
 operator_role TEXT DEFAULT 'historical-record', current_status TEXT, reporting_date DATE,
 polygon_geom GEOMETRY(MultiPolygon,4326), polygon_source_id TEXT REFERENCES research_sources(id),
 source_id TEXT REFERENCES research_sources(id), is_polygon_verified BOOLEAN DEFAULT FALSE,
 CHECK (NOT is_polygon_verified OR (polygon_geom IS NOT NULL AND polygon_source_id IS NOT NULL))
);
CREATE INDEX IF NOT EXISTS idx_concession_geom ON concessions USING GIST(polygon_geom);
CREATE INDEX IF NOT EXISTS idx_concession_block ON concessions(block_number);
CREATE TABLE IF NOT EXISTS field_locations (
 id BIGSERIAL PRIMARY KEY, name TEXT NOT NULL, geom GEOMETRY(Point,4326),
 rock_unit_id TEXT REFERENCES geological_units(id), source_id TEXT REFERENCES research_sources(id),
 visibility TEXT NOT NULL DEFAULT 'public' CHECK (visibility IN ('public','restricted','private'))
);
CREATE INDEX IF NOT EXISTS idx_field_location_geom ON field_locations USING GIST(geom);
CREATE TABLE IF NOT EXISTS dataset_revisions (
 id BIGSERIAL PRIMARY KEY, dataset_name TEXT NOT NULL, source_id TEXT REFERENCES research_sources(id),
 effective_date DATE, imported_at TIMESTAMPTZ DEFAULT now(), checksum_sha256 CHAR(64),
 status TEXT NOT NULL DEFAULT 'pending_review'
);
