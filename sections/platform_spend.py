import streamlit as st
import plotly.express as px

def render_platform_spend(df):

    st.subheader("01. Spend by Platform")
    st.caption("SECTION 01 · MIX")

    platform_spend = df.groupby("platform")["spend"].sum().reset_index()

    fig = px.pie(
        platform_spend,
        names="platform",
        values="spend",
        hole=0.5
    )

    fig.update_traces(
    textinfo="percent+value",
    textfont_color="white"
)

    fig.update_layout(
        showlegend=True,
        legend_title_text="Platform"
    )

    st.plotly_chart(fig, use_container_width=True)