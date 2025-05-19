import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import numpy as np
from geopy.distance import geodesic
from collections import defaultdict
import folium

def render():
    st.title("📍 화성시 안전 점수 격자 지도")

    file_score_map = {
        "data/소방경찰.xlsx": 3,
        "data/유흥.xlsx": -3,
        "data/어린이보호구역.xlsx": 2,
        "data/아동센터.xlsx": 2,
        "data/스쿨존내어린이사고다발지.xlsx": -2,
        "data/성범죄자.xlsx": -3,
    }

    all_points = []

    for path, score in file_score_map.items():
        try:
            df = pd.read_excel(path, engine="openpyxl")

            # 위도/경도 컬럼이 없을 경우 건너뜀
            if {"refine_wgs84_lat", "refine_wgs84_logt"}.issubset(df.columns):
                for _, row in df.iterrows():
                    lat, lon = row["refine_wgs84_lat"], row["refine_wgs84_logt"]
                    if pd.notnull(lat) and pd.notnull(lon):
                        all_points.append((lat, lon, score))
            else:
                st.warning(f"⚠️ '{path}'에는 refine_wgs84_lat / refine_wgs84_logt 컬럼이 없습니다. 건너뜁니다.")

        except Exception as e:
            st.error(f"❌ 파일 '{path}' 읽기 중 오류 발생: {e}")

    if not all_points:
        st.error("❗ 유효한 좌표 데이터를 가진 파일이 없습니다.")
        return

    # 격자 생성
    lat_range = np.arange(36.95, 37.35, 0.001)
    lon_range = np.arange(126.8, 127.3, 0.001)
    grid_points = [(round(lat, 4), round(lon, 4)) for lat in lat_range for lon in lon_range]

    # 그리드 점수 계산
    grid_scores = defaultdict(float)
    for lat_g, lon_g in grid_points:
        scores = [score for lat_p, lon_p, score in all_points if geodesic((lat_g, lon_g), (lat_p, lon_p)).meters <= 200]
        if scores:
            grid_scores[(lat_g, lon_g)] = np.mean(scores)

    if not grid_scores:
        st.warning("⚠️ 그리드 점수가 계산되지 않았습니다.")
        return

    # 색상 계산 함수
    def get_color(score, min_score, max_score):
        ratio = (score - min_score) / (max_score - min_score + 1e-6)
        ratio = max(0, min(1, ratio))
        r = int(255 * (1 - ratio))
        g = int(255 * ratio)
        return f"#{r:02x}{g:02x}00"

    # Folium 지도 생성
    m = folium.Map(location=[37.2, 127.0], zoom_start=11)
    min_score, max_score = min(grid_scores.values()), max(grid_scores.values())

    for (lat, lon), score in grid_scores.items():
        color = get_color(score, min_score, max_score)
        folium.Rectangle(
            bounds=[(lat, lon), (lat + 0.001, lon + 0.001)],
            color=color,
            fill=True,
            fill_opacity=0.6,
            weight=0
        ).add_to(m)

    st_folium(m, width=900, height=700)

