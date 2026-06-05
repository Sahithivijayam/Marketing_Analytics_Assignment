import streamlit as st
import pandas as pd
import plotly.express as px

def render_trend_section(df):

    st.subheader("02 · Daily Trajectory")
    st.caption("SECTION 02 · TIME SERIES")

    df["date"] = pd.to_datetime(df["date"])

    all_dates = sorted(df["date"].unique())

    daily_spend = df.groupby(["date", "platform"])["spend"].sum().reset_index()


    ### Daily Spend
    fig1 = px.line(
        daily_spend,
        x="date",
        y="spend",
        color="platform",
        markers=True
    )

    fig1.update_layout(title="Daily Spend by Platform", xaxis_title="Date",
        yaxis_title="Spend", legend_title="Platform")
    
    fig1.update_xaxes(
        tickmode="array",
        tickvals=all_dates,
        tickformat="%b %d",
        tickangle=-45
    )

    st.plotly_chart(fig1, use_container_width=True)

    ### Daily Conversions
    daily_conv = df.groupby(["date", "platform"])["conversions"].sum().reset_index()

    fig2 = px.line(
        daily_conv,
        x="date",
        y="conversions",
        color="platform",
        markers=True
    )

    fig2.update_layout(title="Daily Conversions by Platform", xaxis_title="Date",
        yaxis_title="Conversions", legend_title="Platform")
    
    fig2.update_xaxes(
        tickmode="array",
        tickvals=all_dates,
        tickformat="%b %d",
        tickangle=-45
    )

    st.plotly_chart(fig2, use_container_width=True)
