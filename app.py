import streamlit as st
from my_pages import page_grid, page_heatmap, page_school

st.set_page_config(page_title="화성시 안전지도", layout="wide")

page = st.sidebar.selectbox("페이지 선택", [
    "📍 격자 타일 기반 안전 시각화",
    "🔥 HeatMap 기반 시각화",
    "🏫 초등학교 주변 경로"
])

if page == "📍 격자 타일 기반 안전 시각화":
    page_grid.render()
elif page == "🔥 HeatMap 기반 시각화":
    page_heatmap.render()
elif page == "🏫 초등학교 주변 경로":
    page_school.render()
