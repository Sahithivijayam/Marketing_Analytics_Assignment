import streamlit as st
import pandas as pd
import plotly.express as px

def render_efficiency_section(df):

    st.subheader("03 · Efficiency, side by side")
    st.caption("SECTION 03 · UNIT ECONOMICS")

  
    platform_df = df.groupby("platform").agg({
        "clicks": "sum",
        "impressions": "sum",
        "spend": "sum",
        "conversions": "sum"
    }).reset_index()

    platform_df["ctr"] = (platform_df["clicks"] / platform_df["impressions"]) * 100
    platform_df["cpc"] = platform_df["spend"] / platform_df["clicks"]
    platform_df["cpa"] = platform_df["spend"] / platform_df["conversions"]
    platform_df["cvr"] = (platform_df["conversions"] / platform_df["clicks"]) * 100

   
    order = ["Facebook", "Google", "TikTok"]
    platform_df["platform"] = pd.Categorical(platform_df["platform"], categories=order, ordered=True)
    platform_df = platform_df.sort_values("platform")

  
    color_map = {
        "Facebook": "#1877F2",
        "Google": "#4285F4",
        "TikTok": "#010101"
    }

   
    col1, col2, col3, col4 = st.columns(4)

    # CTR (Efficiency KPI)
    with col1:
        fig1 = px.bar(
            platform_df,
            x="platform",
            y="ctr",
            text_auto=".2f",
            title="CTR (higher = better)"
        )

        fig1.update_traces(
            marker_color=platform_df["platform"].map(color_map),
            showlegend=False
        )

        fig1.update_layout(
            margin=dict(l=10, r=10, t=40, b=10),
            yaxis_title="CTR (%)"
        )

        fig1.update_yaxes(showgrid=True, gridcolor="rgba(0,0,0,0.1)")
        st.plotly_chart(fig1, use_container_width=True)

    # CPC
    with col2:
        fig2 = px.bar(
            platform_df,
            x="platform",
            y="cpc",
            text_auto="$.2f",
            title="CPC (lower = better)"
        )

        fig2.update_traces(
            marker_color=platform_df["platform"].map(color_map),
            showlegend=False
        )

        fig2.update_layout(
            margin=dict(l=10, r=10, t=40, b=10),
            yaxis_title="CPC ($)"
        )

        fig2.update_yaxes(showgrid=True, gridcolor="rgba(0,0,0,0.1)")
        st.plotly_chart(fig2, use_container_width=True)

    # CPA
    with col3:
        fig3 = px.bar(
            platform_df,
            x="platform",
            y="cpa",
            text_auto=".2f",
            title="CPA (lower = better)"
        )

        fig3.update_traces(
            marker_color=platform_df["platform"].map(color_map),
            showlegend=False
        )

        fig3.update_layout(
            margin=dict(l=10, r=10, t=40, b=10),
            yaxis_title="CPA ($)"
        )

        fig3.update_yaxes(showgrid=True, gridcolor="rgba(0,0,0,0.1)")
        st.plotly_chart(fig3, use_container_width=True)

    # CVR
    with col4:
        fig4 = px.bar(
            platform_df,
            x="platform",
            y="cvr",
            text_auto=".2f",
            title="CVR (higher = better)"
        )

        fig4.update_traces(
            marker_color=platform_df["platform"].map(color_map),
            showlegend=False
        )

        fig4.update_layout(
            margin=dict(l=10, r=10, t=40, b=10),
            yaxis_title="CVR (%)"
        )

        fig4.update_yaxes(showgrid=True, gridcolor="rgba(0,0,0,0.1)")
        st.plotly_chart(fig4, use_container_width=True)