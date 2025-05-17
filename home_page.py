import streamlit as st
from PIL import Image

def show_home_page():
    st.set_page_config(page_title="FinRealm", layout="wide")

    # Project Banner / Title
    col1, col2 = st.columns([1, 4])
    with col1:
       st.image("https://i.imgur.com/UJNmN8T.png", width=220)

    with col2:
        st.markdown(
            "<h1 style='font-size: 50px; color: #33CCCC; font-family:Trebuchet MS;'>FinRealm 💸</h1>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h4 style='color: gray;'>A Multi-Themed Financial Machine Learning App</h4>",
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # Overview Section
    st.subheader("📊 Project Overview")
    st.markdown(
        """
        **FinRealm** is a final semester project built using **Streamlit**, combining **Machine Learning** and **Finance** in a fun and thematic way.  
        Each theme in the app demonstrates a different ML model on financial datasets, using **Kragle** data and **real-time stock data via Yahoo Finance**.
        """
    )

    # Features Grid
    st.subheader("🚀 Features")
    st.markdown(
        """
        - 🔄 Upload CSVs from Kragle datasets  
        - 🌐 Fetch stock data using Yahoo Finance API  
        - 🧠 Apply ML Models: Linear Regression, Logistic Regression, K-Means, Decision Tree  
        - 🎨 Unique visual themes designed by each team member  
        - 📈 Interactive graphs, metrics, and analytics  
        - 🌍 Deployed on Streamlit Cloud  
        """
    )

    st.markdown("---")

    # Themes Teaser
    st.subheader("🎭 Explore Realms")
    st.markdown("Each realm represents a unique theme & ML model:")

    cols = st.columns(4)
    realms = [
        ("Desert Mirage 🏜️", "media/images/desert_theme.png", "Linear Regression"),
        ("Galactic Pulse 🌌", "media/images/galactic_theme.png", "Logistic Regression"),
        ("Cyber Ice ❄️", "media/images/cyber_theme.png", "K-Means Clustering"),
        ("Pixel Quest 🎮", "media/images/pixel_theme.png", "Decision Tree Classifier"),
    ]

    for col, (title, img_path, model) in zip(cols, realms):
        with col:
            st.image(img_path, use_column_width=True)
            st.markdown(f"### {title}")
            st.markdown(f"*Model:* `{model}`")

    st.markdown("---")

    # Tech Stack
    st.subheader("🧰 Tech Stack")
    st.markdown(
        """
        - **Python** 🐍  
        - **Streamlit** for UI  
        - **Scikit-Learn**, **Pandas**, **NumPy** for ML  
        - **Matplotlib**, **Plotly** for Visualization  
        - **yfinance** for fetching stock market data  
        """
    )

    st.markdown("---")

    # Footer
    st.markdown(
        "<center><span style='font-size: 14px; color: #aaa;'>© 2025 FinRealm Team – Final Year Project | FAST NUCES</span></center>",
        unsafe_allow_html=True,
    )
