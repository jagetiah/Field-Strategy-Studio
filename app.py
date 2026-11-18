"""Field Strategy Studio pilot, hosted on Streamlit.

The pilot is a self-contained interactive app (pilot.html) with synthetic data.
This file serves it full-screen inside Streamlit so it can be deployed on
Streamlit Community Cloud or any Streamlit host.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Field Strategy Studio · Pilot",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit chrome and let the pilot fill the window.
st.markdown(
    """
    <style>
      header[data-testid="stHeader"], footer, #MainMenu, [data-testid="stToolbar"],
      [data-testid="stSidebar"], [data-testid="collapsedControl"] { display: none !important; }
      html, body, [data-testid="stApp"], [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        height: 100dvh !important; overflow: hidden !important; padding: 0 !important; margin: 0 !important; }
      [data-testid="stMainBlockContainer"], .block-container {
        padding: 0 !important; max-width: 100% !important; }
      [data-testid="stVerticalBlock"], [data-testid="stElementContainer"] { gap: 0 !important; }
      /* Match the embedded app by tag, because Streamlit changes the iframe title between versions. */
      [data-testid="stMain"] iframe { height: 100dvh !important; width: 100% !important; border: 0; display: block; }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner=False)
def load_app() -> str:
    return Path(__file__).with_name("pilot.html").read_text(encoding="utf-8")


components.html(load_app(), height=900, scrolling=False)
