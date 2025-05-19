import streamlit as st
import plotly.graph_objects as go

def render(all_points):
    st.title("🔥 HeatMap 기반 시각화")
    st.markdown("각 점의 안전 점수를 Plotly 지도 상에 직접 시각화합니다.")

    def classify_score(score):
        if score >= 2:
            return "🟢 안전"
        elif score <= -2:
            return "🔴 위험"
        else:
            return "🟡 보통"

    data = []
    for lat, lon, score in all_points:
        status = classify_score(score)
        data.append({
            "lat": lat,
            "lon": lon,
            "score": score,
            "status": status
        })

    fig = go.Figure(go.Scattermapbox(
        mode="markers",
        lat=[p["lat"] for p in data],
        lon=[p["lon"] for p in data],
        marker=dict(
            size=10,
            color=[p["score"] for p in data],
            colorscale="Viridis",
            cmin=-3, cmax=3,
            colorbar=dict(title="Score")
        ),
        text=[f"위도: {p['lat']:.5f}<br>경도: {p['lon']:.5f}<br>점수: {p['score']}<br>상태: {p['status']}" for p in data],
        hoverinfo="text"
    ))

    fig.update_layout(
        mapbox=dict(
            style="carto-positron",
            center=dict(lat=37.198, lon=127.034),
            zoom=12
        ),
        title="화성시 안전 점수 지도 (Plotly)",
        margin=dict(l=0, r=0, t=40, b=0)
    )

    st.plotly_chart(fig, use_container_width=True)
