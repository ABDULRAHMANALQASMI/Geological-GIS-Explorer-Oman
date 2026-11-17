#!/bin/bash
cd "$(dirname "$0")"
echo "GEO//OMAN V3 — launching static web application"
echo "Open http://localhost:8000 in your browser, press Control+C to stop"
python3 -m http.server 8000
