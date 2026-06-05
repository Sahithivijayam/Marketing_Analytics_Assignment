import streamlit as st
import pandas as pd

def render_campaign_leaderboard(df):

    st.subheader("04 · Campaign Leaderboard")
    st.caption("SECTION 04 · GRANULAR")

    # -------------------------
    # Aggregate at campaign level
    # -------------------------
    camp_df = df.groupby(["platform", "campaign_name"]).agg({
        "spend": "sum",
        "impressions": "sum",
        "clicks": "sum",
        "conversions": "sum"
    }).reset_index()

    # -------------------------
    # Derived metrics
    # -------------------------
    camp_df["cpc"] = camp_df["spend"] / camp_df["clicks"]
    camp_df["cpa"] = camp_df["spend"] / camp_df["conversions"]
    camp_df["cvr"] = (camp_df["conversions"] / camp_df["clicks"]) * 100

    # -------------------------
    # Sort (best campaigns first)
    # -------------------------
    camp_df = camp_df.sort_values("conversions", ascending=False)

    # -------------------------
    # Final display columns
    # -------------------------
    display_df = camp_df[
        [
            "platform",
            "campaign_name",
            "spend",
            "impressions",
            "clicks",
            "conversions",
            "cpc",
            "cpa",
            "cvr"
        ]
    ]

    # -------------------------
    # Clean table (NO INDEX)
    # -------------------------
    st.dataframe(
        display_df.reset_index(drop=True).style.format({
            "spend": "${:,.2f}",
            "cpc": "${:.2f}",
            "cpa": "${:.2f}",
            "cvr": "{:.2f}%"
        }),
        use_container_width=True
    )