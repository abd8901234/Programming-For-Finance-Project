import streamlit as st
from welcome import show_welcome
from Themes.wallstreet_theme import show_wallstreet_theme
from Themes.retro_theme import show_retro_theme
from Themes.eco_theme import show_eco_theme
from Themes.space_theme import show_space_theme

# 🚀 New project name!
PROJECT_NAME = "Finance Multiverse"

st.set_page_config(
    page_title=PROJECT_NAME,
    layout="wide",
    initial_sidebar_state="expanded",
)

# Use online logo (or assets/logo.png if local)
LOGO_URL = "https://cdn-icons-png.flaticon.com/512/2230/2230957.png"

st.sidebar.image(LOGO_URL, width=110, caption=PROJECT_NAME)
st.sidebar.title(f"🌌 {PROJECT_NAME}")

pages = {
    "Welcome": show_welcome,
    "Wall Street Theme (Linear Regression)": show_wallstreet_theme,
    "Retro 80s Theme (Logistic Regression)": show_retro_theme,
    "Eco Theme (K-Means)": show_eco_theme,
    "Space Theme (Linear Regression)": show_space_theme,
}

choice = st.sidebar.radio("Navigate", list(pages.keys()))
pages[choice]()

st.markdown("""
    <hr>
    <center>
        <small>Made with ❤️ by [Your Group Names] for Programming for Finance (AF3005), FAST-NUCES, Spring 2025.<br>
        Project: <b>Finance Multiverse</b>
        </small>
    </center>
    """, unsafe_allow_html=True)
