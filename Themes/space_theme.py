import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from utils import load_kaggle_data, fetch_yahoo_data, space_theme_style

def show_space_theme():
    space_theme_style()
    st.markdown("""
        <h2>🚀 Space Exploration Theme: Linear Regression</h2>
        <img src="https://media.giphy.com/media/WFZvB7VIXBgiz3oDXE/giphy.gif" width="250">
        <p style="font-family: 'Orbitron', sans-serif; font-size:17px;">
        Blast off into the financial cosmos—explore your data at light speed!
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
        st.success("Data loaded! Prepare for launch.")
        st.write(data.head(10))
        st.header("Step 2: Linear Regression Model", divider='rainbow')
        cols = data.select_dtypes(include=np.number).columns.tolist()
        if len(cols) < 2:
            st.error("At least two numeric columns are required for regression.")
            return
        x_col = st.selectbox("Select X (Feature)", cols, key="space_x")
        y_col = st.selectbox("Select Y (Target)", [col for col in cols if col != x_col], key="space_y")
        if st.button("Run Linear Regression 🛸", key="space_regress"):
            X = data[[x_col]].values
            y = data[y_col].values
            model = LinearRegression().fit(X, y)
            y_pred = model.predict(X)
            r2 = model.score(X, y)
            # Visualize
            fig, ax = plt.subplots(figsize=(7,5))
            ax.scatter(X, y, c="#fad744", alpha=0.7, label="Actual")
            ax.plot(X, y_pred, color="#5f5fff", lw=3, label="Predicted")
            ax.set_facecolor("#22223b")
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            ax.set_title("Space Linear Regression", color="#fad744")
            ax.legend()
            st.pyplot(fig)
            st.success(f"R² Score: {r2:.3f}")
            st.info(f"Regression Equation: {y_col} = {model.coef_[0]:.2f} × {x_col} + {model.intercept_:.2f}")

        st.markdown("""
        <img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" width="180">
        <p>Houston, we have a prediction! 🚀</p>
        """, unsafe_allow_html=True)
