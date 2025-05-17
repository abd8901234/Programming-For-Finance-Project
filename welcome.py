import streamlit as st

def show_welcome():
    st.markdown("""
    <style>
    .big-font {font-size:30px !important;}
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="big-font"><b>💹 Multi-Themed Financial ML App</b></div>', unsafe_allow_html=True)
    st.write("---")

    st.info("**Welcome! Explore finance ML with four original, interactive themes. Each offers unique visuals, features, and a dedicated ML model.**")

    st.image("assets/main_banner.png", caption="Unleash the power of financial data in four creative styles!", use_container_width=True)

    st.write("### 🏛️ Wall Street | 🕹️ Retro 80s | 🌳 Eco Nature | 🚀 Space")
    st.write("""
    - **Upload your own Kaggle CSV, or fetch real-time data from Yahoo Finance in each theme.**
    - Unique models: Linear Regression, Logistic Regression, K-Means, Decision Tree.
    - Use the sidebar to select a theme and explore!
    """)

    st.write("#### Meet the Developers")
    st.markdown("""
    - [Abdullah Nawaz] — Wall Street Theme
    - [Mohsin Ali] — Retro 80s Theme
    - [Hamza Abbasi] — Eco Theme
    - [Combined] — Space Theme
    """)

    st.success("Start exploring! Choose a theme from the sidebar.")
    st.write("---")
    st.markdown("""
    <small>
    _Instructor: Dr. Usama Arshad_  
    _Course: Programming for Finance (AF3005)_
    </small>
    """, unsafe_allow_html=True)
