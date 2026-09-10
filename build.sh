#!/bin/sh
# Bouwt docs/index.html — de standalone versie voor GitHub Pages.
# index.html is de artifact-bron (zonder <html>/<head>/<body>: die voegt
# claude.ai zelf toe bij publiceren). Pages heeft wel een volledig document
# nodig, met charset en viewport. Draai dit na elke wijziging in index.html.
python3 build.py
