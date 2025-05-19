import streamlit as st

# ✅ 반드시 가장 첫 줄에서 설정
st.set_page_config(page_title="화성시 안전지도", layout="wide")

# 그 이후에 다른 import 및 실행 코드
import os
import streamlit.components.v1 as components

st.title("📍 화성시 안전 점수 격자 지도")

html_path = "static/grid_map.html"
if os.path.exists(html_path):
    st.markdown("아래는 미리 생성된 folium 기반 격자 지도입니다.")
    components.iframe(html_path, height=700, scrolling=True)
    with open(html_path, "rb") as f:
        st.download_button("🧾 HTML 지도 다운로드", f, file_name="화성시_격자_지도.html")
else:
    st.error("⚠️ grid_map.html 파일이 static 폴더에 없습니다.")
