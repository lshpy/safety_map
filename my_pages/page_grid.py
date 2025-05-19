import streamlit as st
from streamlit_folium import st_folium
import folium
import os

def render():
    st.set_page_config(page_title="화성시 안전지도", layout="wide")
    st.title("📍 화성시 안전 점수 격자 지도")

    html_path = "static/grid_map.html"
    if os.path.exists(html_path):
        # ✅ folium 지도 HTML 직접 불러오기
        with open(html_path, "r", encoding="utf-8") as f:
            html_str = f.read()
        # ✅ st_folium으로 렌더링
        st.components.v1.html(html_str, height=700)
        # 다운로드 버튼
        with open(html_path, "rb") as f:
            st.download_button("🧾 HTML 지도 다운로드", f, file_name="화성시_격자_지도.html")
    else:
        st.error("⚠️ static/grid_map.html 파일이 없습니다.")
