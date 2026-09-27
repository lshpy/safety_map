---
title: "child_safety_map"
emoji: "🛡️"
colorFrom: "blue"
colorTo: "green"
sdk: "streamlit"
sdk_version: "1.32.0"
app_file: "app.py"
pinned: false
---

# Hwaseong City Children's Safety Map (화성시 안전지도)

> Streamlit app that visualizes safety information for children in Hwaseong City, Korea.

**The app's user interface is in Korean.**

## What it does

Location data on safety-related facilities and risks in Hwaseong are combined into a point-based safety score
and shown on interactive maps. Each data file gets a fixed score (`utils.py`): police/fire stations +3,
child protection zones +2, children's centres +2, frequent child-accident spots in school zones -2,
entertainment venues -3, registered sex offenders -3.

- 📍 Grid-tile safety map: average score of points within 200 m of each grid cell
- 🔥 Point map of safety scores (safe / normal / danger)
- 🏫 Safety routes around elementary schools (pre-rendered map)

## Repository layout

| Path | Content |
|---|---|
| `app.py` | Entry point with page selector |
| `my_pages/` | The three map pages (`page_grid.py`, `page_heatmap.py`, `page_school.py`) |
| `utils.py` | Data loading, grid scoring and colour helpers |
| `data/*.xlsx` | Input data: police/fire stations, entertainment venues, child protection zones, children's centres, school-zone accident spots, sex offenders, elementary schools |
| `static/*.html` | Pre-rendered Folium maps (grid, heat map, school routes) |
| `Dockerfile` | Container for Hugging Face Spaces (port 7860) |

## How to run (local)

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Status

Policy competition entry, 2025.

---
https://github.com/lshpy
