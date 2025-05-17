import streamlit as st
from realms.pixel_quest import show_pixel_quest
from realms.cyber_ice import cyber_ice_theme
from realms.desert_mirage import desert_mirage_theme
from realms.galactic_pulse import galactic_pulse_theme
from realms.home_page import show_home_page

# App Configurations
st.set_page_config(
    page_title="FinRealm - Multi-Themed Financial Intelligence",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="💼",
)

# Sidebar for Navigation
with st.sidebar:
    st.image("resources/images/finrealm_logo.png", width=220)
    st.title("🔮 FinRealm")
    st.markdown("Navigate through financial realms:")
    selected_section = st.radio(
        "Choose a Realm:",
        (
            "🏠 Welcome",
            "🏜️ Desert Mirage (Linear Regression)",
            "🪐 Galactic Pulse (Logistic Regression)",
            "❄️ Cyber Ice (K-Means Clustering)",
            "🕹️ Pixel Quest (Decision Tree)",
        ),
        index=0
    )

# Main Area - Routing Views
if selected_section == "🏠 Welcome":
    show_home_page()

elif selected_section == "🏜️ Desert Mirage (Linear Regression)":
    desert_mirage_theme()

elif selected_section == "🪐 Galactic Pulse (Logistic Regression)":
    galactic_pulse_theme()

elif selected_section == "❄️ Cyber Ice (K-Means Clustering)":
    cyber_ice_theme()

elif selected_section == "🕹️ Pixel Quest (Decision Tree)":
    show_pixel_quest()
