import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import time

def show_pixel_quest():
    st.markdown(
        """
        <style>
        .main {
            background-color: #1f1f2e;
            color: #f2f2f2;
            font-family: 'Press Start 2P', cursive;
        }
        </style>
        <link href='https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap' rel='stylesheet'>
        """,
        unsafe_allow_html=True
    )

    st.title("🎮 Pixel Quest Realm")
    st.markdown("#### Retro Gaming Meets Financial Clustering")

    st.markdown(
        "Step into a pixelated world of financial patterns! This theme leverages **K-Means Clustering** "
        "to discover hidden groupings in financial data — all styled in classic 8-bit arcade vibes."
    )

    st.image("media/images/pixel_banner.png", use_column_width=True)

    st.markdown("### 📁 Upload Financial Data")
    uploaded_file = st.file_uploader("Upload a Kragle financial dataset (CSV)", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
        st.dataframe(df.head())

        st.markdown("### 🎯 Select Features for Clustering")
        numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

        if len(numeric_cols) < 2:
            st.error("Need at least 2 numeric columns for clustering.")
            return

        x_col = st.selectbox("X-axis Feature", options=numeric_cols)
        y_col = st.selectbox("Y-axis Feature", options=[col for col in numeric_cols if col != x_col])

        num_clusters = st.slider("Select Number of Clusters", min_value=2, max_value=10, value=3)

        if st.button("🧠 Run K-Means Clustering"):
            with st.spinner("Clustering coins, finding patterns..."):
                time.sleep(2)

                X = df[[x_col, y_col]].dropna()
                scaler = StandardScaler()
                X_scaled = scaler.fit_transform(X)

                kmeans = KMeans(n_clusters=num_clusters, random_state=42)
                labels = kmeans.fit_predict(X_scaled)

                X["Cluster"] = labels
                df["Cluster"] = labels

                fig = px.scatter(
                    X,
                    x=x_col,
                    y=y_col,
                    color=X["Cluster"].astype(str),
                    title="🎯 Pixel Quest Clusters",
                    template="plotly_dark",
                    color_discrete_sequence=px.colors.qualitative.Pastel
                )
                st.plotly_chart(fig, use_container_width=True)

                st.markdown("### 📊 Cluster Summary")
                st.write(df.groupby("Cluster")[[x_col, y_col]].mean())

                st.balloons()

    else:
        st.warning("Please upload a CSV file to begin your quest!")

    st.markdown("---")
    st.markdown("🕹️ *Inspired by retro gaming aesthetics, powered by data science.*")

