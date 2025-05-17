import streamlit as st
from realms.desert_mirage import desert_mirage_theme
from realms.galactic_pulse import galactic_pulse_theme
from realms.cyber_ice import cyber_ice_theme
from realms.pixel_quest import pixel_quest_theme
from home_page import show_home_page

# Set page config
st.set_page_config(
    page_title="FinRealm - Financial ML Realms",
    layout="wide",
    page_icon="💸"
)

# Sidebar - App Navigation
st.sidebar.title("🔮 FinRealm Navigation")
page = st.sidebar.selectbox("Choose a Realm", [
    "🏠 Home",
    "🏜 Desert Mirage (Linear Regression)",
    "🚀 Galactic Pulse (Logistic Regression)",
    "🧊 Cyber Ice (K-Means Clustering)",
    "🎮 Pixel Quest (Decision Tree)"
])

# Load data via sidebar options
st.sidebar.markdown("---")
st.sidebar.subheader("📈 Load Financial Data")
data = load_data()

# Display selected page
if page == "🏠 Home":
    show_home_page()

elif page == "🏜 Desert Mirage (Linear Regression)":
    desert_mirage_theme(data)

elif page == "🚀 Galactic Pulse (Logistic Regression)":
    galactic_pulse_theme(data)

elif page == "🧊 Cyber Ice (K-Means Clustering)":
    cyber_ice_theme(data)

elif page == "🎮 Pixel Quest (Decision Tree)":
    pixel_quest_theme(data)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: grey;'>© 2025 FinRealm Project | Built for Programming for Finance - Final Semester</p>",
    unsafe_allow_html=True
)
