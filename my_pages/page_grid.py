# page_grid.py
import streamlit as st
from streamlit_folium import st_folium  # or components.v1.html
import os

def render():
    st.title("📍 화성시 안전 점수 격자 지도")

    html_path = "static/grid_map.html"
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            html_str = f.read()
        st.components.v1.html(html_str, height=700)
        with open(html_path, "rb") as f:
            st.download_button("🧾 HTML 지도 다운로드", f, file_name="화성시_격자_지도.html")
    else:
        st.error("⚠
