import streamlit as st

def render_takeaways():

    st.subheader("05 · What the data is saying")
    st.caption("SECTION 05 · TAKEAWAYS")

    col1, col2, col3 = st.columns(3)

    card_style = """
        border:1px solid #e6e6e6;
        border-radius:12px;
        padding:16px;
        background-color:white;
        color:#111;
        height:auto;
        min-height:180px;
        box-shadow:0 2px 8px rgba(0,0,0,0.05);
    """

    with col1:
        st.markdown(f"""
        <div style="{card_style}">
        <h1 style="color:#1f77b4;margin:0;">01</h1>
        <h4>Facebook HAS THE LOWEST CPA</h4>
        <p style="font-size:13px;line-height:1.4;">
        At $7.64 per conversion, Facebook is 31% more efficient than the worst-cost channel.<br>
        Tilt budget here if conversion volume is the goal.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="{card_style}">
        <h1 style="color:#d62728;margin:0;">02</h1>
        <h4>TikTok: Reach, not Revenue</h4>
        <p style="font-size:13px;line-height:1.4;">
        TikTok drives high impressions but weak conversion efficiency.<br>
        Strong top-of-funnel signal, needs mid-funnel optimization.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style="{card_style}">
        <h1 style="color:#ff7f0e;margin:0;">03</h1>
        <h4>Biggest Single Bet</h4>
        <p style="font-size:13px;line-height:1.4;">
        One campaign absorbed highest spend and delivered strong efficiency.<br>
        Key driver of total conversions.
        </p>
        </div>
        """, unsafe_allow_html=True)