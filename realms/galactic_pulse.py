"""
Galactic Pulse Theme Module
Logistic Regression for Market Movement Direction Prediction
Author: YourName
Date: 2025-05-17

Description:
This module implements the Galactic Pulse theme with neon colors and space vibes.
It predicts if the stock price will go up or down the next day using Logistic Regression.
Includes interactive features and probability visualization.
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

def galactic_pulse_theme(data: pd.DataFrame):
    """Run the Galactic Pulse themed logistic regression analysis."""

    st.markdown(
        """
        <style>
        .title {
            color: #39FF14; 
            font-family: 'Orbitron', sans-serif; 
            font-size: 3.8rem; 
            text-shadow: 0 0 15px #39FF14, 0 0 30px #0F0;
        }
        .subtitle {
            color: #72FF97; 
            font-family: 'Orbitron', sans-serif;
            font-size: 1.7rem;
            margin-bottom: 25px;
        }
        .info {
            color: #00FF99;
            font-family: 'Orbitron', sans-serif;
        }
        .conf-matrix {
            background-color: #111;
            border-radius: 8px;
            padding: 15px;
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown('<h1 class="title">🚀 Galactic Pulse Realm</h1>', unsafe_allow_html=True)
    st.markdown('<h3 class="subtitle">Predicting Market Movement Using Logistic Regression</h3>', unsafe_allow_html=True)
    st.image("static_files/gifs/space_neon.gif", width=350)

    if data.empty:
        st.warning("No data loaded. Please upload a dataset or select a ticker with valid data.")
        return

    # Check for 'Close' column
    if 'Close' not in data.columns:
        st.error("Dataset must contain 'Close' column.")
        return

    # Prepare the dataset
    df = data[['Close']].dropna().copy()

    # Create target variable: 1 if next day's close > today's close else 0
    df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
    df.dropna(inplace=True)

    # Feature engineering: use 'Close' price today as feature
    X = df[['Close']]
    y = df['Target']

    # Train/test split with shuffle = False to respect time series
    test_size = st.slider("Test Set Size (%)", min_value=10, max_value=50, value=25, step=5)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size/100, shuffle=False)

    # Model initialization and training
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # Predictions and probabilities
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    # Evaluation metrics
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)

    st.markdown(f'<p class="info"><strong>Test Set Size:</strong> {test_size}%</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="info"><strong>Accuracy:</strong> {accuracy:.3f}</p>', unsafe_allow_html=True)

    # Confusion Matrix Plot
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='inferno', cbar=False, ax=ax)
    ax.set_title("Confusion Matrix", fontsize=16, color='#39FF14')
    ax.set_xlabel("Predicted Label")
    ax.set_ylabel("True Label")
    st.pyplot(fig)

    # Show classification report
    st.write("### Classification Report:")
    st.text(classification_report(y_test, y_pred))

    # Probability distribution plot
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    sns.histplot(y_prob, bins=25, color='#00FF99', kde=True, ax=ax2)
    ax2.set_title("Predicted Probability Distribution for Price Increase", fontsize=14, color='#39FF14')
    ax2.set_xlabel("Probability")
    ax2.set_ylabel("Frequency")
    st.pyplot(fig2)

    # Optional: Model coefficients display
    st.markdown(
        f'<p class="info"><strong>Model Coefficient:</strong> {model.coef_[0][0]:.4f}</p>', 
        unsafe_allow_html=True)
    st.markdown(
        f'<p class="info"><strong>Model Intercept:</strong> {model.intercept_[0]:.4f}</p>', 
        unsafe_allow_html=True)
