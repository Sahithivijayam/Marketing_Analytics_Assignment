import streamlit as st
from db import get_data
from sections.kpi_section import render_kpis
from sections.platform_spend import render_platform_spend
from sections.daily_trend_section import render_trend_section
from sections.efficiency_section import render_efficiency_section
from sections.campaign_leaderboard import render_campaign_leaderboard
from sections.takeaways_section import render_takeaways





st.set_page_config(layout="wide")

st.title("Marketing Dashboard")

df = get_data()

### section 1: KPIs
st.markdown("""
<style>
.metric-card {
    background-color: white;
    padding: 16px;
    border-radius: 12px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)
render_kpis(df)

### section 2: platform spend
render_platform_spend(df)

### section 3: daily trends
render_trend_section(df)

### section 4: efficiency side by side
render_efficiency_section(df)

### section 5: campaign leaderboard
render_campaign_leaderboard(df)

### section 6: takeaways
render_takeaways()