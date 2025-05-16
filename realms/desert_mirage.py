"""
Desert Mirage Theme Module
Linear Regression on Financial Closing Prices with Interactive Visualization
Author: YourName
Date: 2025-05-17

Description:
This module implements a themed Streamlit app section that applies a Linear Regression model
to predict the closing price of a financial asset using time as the independent variable.
The theme is inspired by desert tones, warm colors, and sand dunes GIFs for immersive UX.
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

def desert_mirage_theme(data: pd.DataFrame):
    """Run the Desert Mirage themed ML analysis and visualization."""
    
    st.markdown(
        """
        <style>
        .title {
            color: #C19A6B; 
            font-family: 'Georgia', serif; 
            font-size: 3.5rem; 
            text-shadow: 2px 2px 4px #A0522D;
        }
        .subtitle {
            color: #DEB887; 
            font-family: 'Palatino Linotype', serif;
            font-size: 1.5rem;
            margin-bottom: 20px;
        }
        .info {
            color: #8B4513;
            font-family: 'Palatino Linotype', serif;
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown('<h1 class="title">🏜 Desert Mirage Realm</h1>', unsafe_allow_html=True)
    st.markdown('<h3 class="subtitle">Predicting Closing Prices Using Linear Regression</h3>', unsafe_allow_html=True)
    st.image("static_files/gifs/desert_sands.gif", width=350)

    if data.empty:
        st.warning("No data loaded. Please upload a dataset or select a ticker with valid data.")
        return

    # Ensure 'Close' column exists
    if 'Close' not in data.columns:
        st.error("Dataset must contain 'Close' column.")
        return

    # Preprocessing: Drop missing values
    df = data[['Close']].dropna().copy()

    # Feature Engineering:
    # Use index converted to ordinal (int) as time feature for regression
    df['DateOrdinal'] = df.index.to_series().apply(lambda x: x.toordinal())
    
    # Interactive slider for test size
    test_size = st.slider("Test Set Size (%)", min_value=10, max_value=50, value=20, step=5)
    
    # Split data
    X = df[['DateOrdinal']]
    y = df['Close']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size/100, shuffle=False)

    # Train Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict on test set
    y_pred = model.predict(X_test)

    # Metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    st.markdown(f'<p class="info"><strong>Test Set Size:</strong> {test_size}%</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="info"><strong>Mean Squared Error (MSE):</strong> {mse:.2f}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="info"><strong>R² Score:</strong> {r2:.2f}</p>', unsafe_allow_html=True)

    # Plotting actual vs predicted
    plt.style.use('seaborn-dark-palette')
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(y_test.index, y_test.values, label='Actual Close', color='#C19A6B', linewidth=2)
    ax.plot(y_test.index, y_pred, label='Predicted Close', color='#DEB887', linestyle='--', linewidth=2)
    ax.set_title('Linear Regression: Actual vs Predicted Closing Prices', fontsize=16, color='#A0522D')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)

    st.pyplot(fig)

    # Optional: Show model coefficients and intercept
    st.markdown(
        f'<p class="info"><strong>Model Coefficient (Slope):</strong> {model.coef_[0]:.4f}</p>', 
        unsafe_allow_html=True)
    st.markdown(
        f'<p class="info"><strong>Model Intercept:</strong> {model.intercept_:.2f}</p>', 
        unsafe_allow_html=True)
