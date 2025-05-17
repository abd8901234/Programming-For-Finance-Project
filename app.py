import streamlit as st
from welcome import show_welcome
from themes.wallstreet_theme import show_wallstreet_theme
from themes.retro_theme import show_retro_theme
from themes.eco_theme import show_eco_theme
from themes.space_theme import show_space_theme

st.set_page_config(
    page_title="Finance ML Multi-Theme",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("💹 Finance ML Multi-Theme App")
st.sidebar.image("assets/logo.png", width=130, caption="Powered by Streamlit")

pages = {
    "Welcome": show_welcome,
    "Wall Street Theme (Linear Regression)": show_wallstreet_theme,
    "Retro 80s Theme (Logistic Regression)": show_retro_theme,
    "Eco Theme (K-Means)": show_eco_theme,
    "Space Theme (Decision Tree)": show_space_theme,
}

choice = st.sidebar.radio("Navigate", list(pages.keys()))

pages[choice]()

st.markdown("""
    <hr>
    <center>
        <small>Made with ❤️ by [Your Group Names] for Programming for Finance (AF3005), FAST-NUCES, Spring 2025.</small>
    </center>
    """, unsafe_allow_html=True)
