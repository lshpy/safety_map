import pandas as pd
import numpy as np
from collections import defaultdict
from geopy.distance import geodesic

# Safety score per data file (keyed by path)
file_score_map = {
    "data/소방경찰.xlsx": 3,
    "data/유흥.xlsx": -3,
    "data/어린이보호구역.xlsx": 2,
    "data/아동센터.xlsx": 2,
    "data/스쿨존내어린이사고다발지.xlsx": -2,
    "data/성범죄자.xlsx": -3,
}

def load_data():
    all_points = []
    for path, score in file_score_map.items():
        df = pd.read_excel(path, engine="openpyxl")
        if {"refine_wgs84_lat", "refine_wgs84_logt"}.issubset(df.columns):
            for _, row in df.iterrows():
                lat, lon = row["refine_wgs84_lat"], row["refine_wgs84_logt"]
                if pd.notnull(lat) and pd.notnull(lon):
                    all_points.append((lat, lon, score))
    return all_points

def calculate_grid_scores(all_points):
    grid_scores = defaultdict(float)
    lat_step, lon_step = 0.001, 0.001
    lat_range = np.arange(36.95, 37.35, lat_step)
    lon_range = np.arange(126.8, 127.3, lon_step)
    grid_points = [(round(lat, 4), round(lon, 4)) for lat in lat_range for lon in lon_range]

    for lat_g, lon_g in grid_points:
        scores = []
        for lat_p, lon_p, score in all_points:
            if geodesic((lat_g, lon_g), (lat_p, lon_p)).meters <= 200:
                scores.append(score)
        if scores:
            grid_scores[(lat_g, lon_g)] = np.mean(scores)

    return grid_scores, grid_points

def get_color(score, min_score, max_score):
    ratio = (score - min_score) / (max_score - min_score + 1e-6)
    ratio = max(0, min(1, ratio))
    r = int(255 * (1 - ratio))
    g = int(255 * ratio)
    return f"#{r:02x}{g:02x}00"

def classify_score(score):
    if score >= 2:
        return "🟢 안전"
    elif score <= -2:
        return "🔴 위험"
    else:
        return "🟡 보통"
