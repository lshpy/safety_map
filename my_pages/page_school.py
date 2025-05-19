import streamlit as st
import streamlit.components.v1 as components

def render():
    st.title("🏫 초등학교 주변 안전 경로 시각화")
    st.markdown("500m~1km 반경 내의 안전지점을 기반으로 한 학교별 경로 시각화입니다.")

    components.iframe("static/school_paths_map.html", height=700, scrolling=True)

    with open("static/school_paths_map.html", "rb") as f:
        st.download_button("🧾 HTML 지도 다운로드", f, file_name="화성시_초등학교_경로.html")
