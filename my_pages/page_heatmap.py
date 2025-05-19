import streamlit as st
import streamlit.components.v1 as components

def render():
    st.title("🔥 HeatMap 기반 시각화")
    st.markdown("사전 계산된 folium HeatMap을 불러와 시각화합니다.")

    components.iframe("static/heat_map.html", height=700, scrolling=True)

    with open("static/heat_map.html", "rb") as f:
        st.download_button("🧾 HTML 지도 다운로드", f, file_name="화성시_HeatMap.html")
