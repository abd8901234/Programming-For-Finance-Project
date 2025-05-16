"""
Cyber Ice Theme Module
K-Means Clustering for Stock Return Patterns
Author: YourName
Date: 2025-05-17

Description:
This module applies K-Means clustering on daily returns of stock prices.
Theme inspired by icy cyber aesthetics: cool blues, pixel art snowflakes.
Interactive cluster number selection and visualization included.
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

def cyber_ice_theme(data: pd.DataFrame):
    """Run the Cyber Ice themed K-Means clustering analysis."""

    st.markdown(
        """
        <style>
        .title {
            color: #00FFFF; 
            font-family: 'Courier New', Courier, monospace; 
            font-size: 3.8rem; 
            text-shadow: 0 0 12px #00FFFF, 0 0 20px #0FF;
        }
        .subtitle {
            color: #66FFFF; 
            font-family: 'Courier New', Courier, monospace;
            font-size: 1.8rem;
            margin-bottom: 25px;
        }
        .info {
            color: #33CCFF;
            font-family: 'Courier New', Courier, monospace;
        }
        .cluster-plot {
            background-color: #0a1624;
            border-radius: 10px;
            padding: 15px;
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown('<h1 class="title">❄️ Cyber Ice Realm</h1>', unsafe_allow_html=True)
    st.markdown('<h3 class="subtitle">Clustering Stock Returns with K-Means</h3>', unsafe_allow_html=True)
    st.image("static_files/gifs/ice_pixel.gif", width=320)

    if data.empty:
        st.warning("No data loaded. Please upload a dataset or select a ticker with valid data.")
        return

    if 'Close' not in data.columns:
        st.error("Dataset must contain 'Close' column.")
        return

    # Compute daily returns
    df = data[['Close']].copy()
    df['Returns'] = df['Close'].pct_change()
    df.dropna(inplace=True)

    # Feature matrix: daily returns reshaped as needed
    X = df[['Returns']].values

    # User input: number of clusters
    n_clusters = st.slider("Select Number of Clusters (k)", min_value=2, max_value=10, value=4)

    # Fit K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(X)

    df['Cluster'] = labels

    # Show cluster sizes
    st.markdown('<p class="info"><strong>Cluster Sizes:</strong></p>', unsafe_allow_html=True)
    cluster_counts = df['Cluster'].value_counts().sort_index()
    st.write(cluster_counts)

    # Plot clustering result: Returns vs Cluster
    fig, ax = plt.subplots(figsize=(10,5))
    palette = sns.color_palette("cool", n_clusters)
    sns.scatterplot(x=df.index, y='Returns', hue='Cluster', data=df, palette=palette, ax=ax, legend='full', s=40)
    ax.set_title("Daily Returns Clustered by K-Means", fontsize=16, color='#00FFFF')
    ax.set_xlabel("Date")
    ax.set_ylabel("Daily Return")
    ax.legend(title='Cluster', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(True, linestyle='--', alpha=0.5)
    st.pyplot(fig)

    # Cluster centers display
    centers = kmeans.cluster_centers_
    centers_df = pd.DataFrame(centers, columns=['Return'])
    centers_df.index.name = 'Cluster'
    st.markdown('<p class="info"><strong>Cluster Centers (Mean Return):</strong></p>', unsafe_allow_html=True)
    st.dataframe(centers_df.style.background_gradient(cmap='cool'))

    # Additional info / tips
    st.info(
        "K-Means clustering groups days with similar return patterns. "
        "You can adjust 'k' to explore different clustering granularities."
    )
