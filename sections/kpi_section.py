import streamlit as st

def render_kpis(df):

    total_spend = df["spend"].sum()
    total_impressions = df["impressions"].sum()
    total_clicks = df["clicks"].sum()
    total_conversions = df["conversions"].sum()

    ctr = (total_clicks / total_impressions) * 100
    cvr = (total_conversions / total_clicks) * 100
    cpa = total_spend / total_conversions

    col1, col2 = st.columns(2)

    with col1:
        st.metric("TOTAL SPEND", f"${total_spend:,.2f}")
        st.caption(f"30-day media investment")

    with col2:
        st.metric("IMPRESSIONS", f"{total_impressions:,}")
        st.caption(f"{ctr:.2f}% blended CTR")

    col3, col4 = st.columns(2)

    with col3:
        st.metric("CONVERSIONS", f"{total_conversions:,}")
        st.caption(f"{cvr:.2f}% BLENDED CVR")

    with col4:
        st.metric("BLENDED CPA", f"${cpa:.2f}")
        st.caption(f"Cost per conversion")