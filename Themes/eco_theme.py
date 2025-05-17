import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from utils import load_kaggle_data, fetch_yahoo_data, eco_theme_style

def show_eco_theme():
    eco_theme_style()
    st.markdown("""
        <h2>🌳 Eco/Nature Theme: K-Means Clustering</h2>
        <img src="https://media.giphy.com/media/XIqCQx02E1U9W/giphy.gif" width="260">
        <p style="font-family: 'Trebuchet MS', Verdana, sans-serif; font-size:17px;">
        Grow your financial knowledge—cluster your data like a thriving forest! 
        </p>
    """, unsafe_allow_html=True)

    data = None
    st.header("Step 1: Load Data (Kaggle or Yahoo Finance)", divider='rainbow')
    with st.expander("Upload Kaggle CSV", expanded=True):
        data = load_kaggle_data()
    if not data:
        with st.expander("Or Fetch Yahoo Finance Data"):
            data = fetch_yahoo_data()
    
    if data is not None:
        st.success("Data loaded! Let's plant some clusters.")
        st.write(data.head(10))
        st.header("Step 2: K-Means Clustering", divider='rainbow')
        cols = data.select_dtypes(include=np.number).columns.tolist()
        if len(cols) < 2:
            st.error("Need at least two numeric columns for clustering!")
            return
        selected_cols = st.multiselect("Select columns for clustering (choose 2 for best plot)", cols, default=cols[:2], key="eco_cols")
        n_clusters = st.slider("Number of Clusters (k)", min_value=2, max_value=6, value=3)
        if st.button("Run K-Means 🍃", key="eco_kmeans"):
            X = data[selected_cols].dropna().values
            if X.shape[1] < 2:
                st.error("Select at least 2 columns for clustering and visualization.")
                return
            kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=0).fit(X)
            labels = kmeans.labels_
            # Visualize
            fig, ax = plt.subplots(figsize=(7,5))
            scatter = ax.scatter(X[:,0], X[:,1], c=labels, cmap='viridis', s=60, alpha=0.7)
            centers = kmeans.cluster_centers_
            ax.scatter(centers[:,0], centers[:,1], c='red', s=100, marker='X', label="Centers")
            ax.set_xlabel(selected_cols[0])
            ax.set_ylabel(selected_cols[1])
            ax.set_title("Eco K-Means Clustering", color="#145a32")
            ax.legend()
            st.pyplot(fig)
            st.success(f"Clustered into {n_clusters} groups! Explore how financial features group together.")

        st.markdown("""
        <img src="https://media.giphy.com/media/LmNwrBhejkK9EFP504/giphy.gif" width="180">
        <p>Trees, leaves, and... data clusters!</p>
        """, unsafe_allow_html=True)
