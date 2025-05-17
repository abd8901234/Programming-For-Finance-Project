import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from utils import load_kaggle_data, fetch_yahoo_data, wallstreet_theme_style

def show_wallstreet_theme():
    wallstreet_theme_style()
    st.markdown("""
        <h2>🏛️ Wall Street Theme: Linear Regression</h2>
        <img src='https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif' width='300'>
        <p style='font-family:Georgia,serif;font-size:17px;'>
        Experience the thrill of Wall Street! Analyze stock data, spot trends, and predict the next bull run.  
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
        st.success("Data loaded! Here is a quick peek:")
        st.write(data.head(10))
        st.header("Step 2: Linear Regression Model", divider='rainbow')
        cols = data.select_dtypes(include=np.number).columns.tolist()
        if len(cols) < 2:
            st.error("Need at least two numeric columns for regression!")
            return
        x_col = st.selectbox("Select X (Feature)", cols, key="ws_x")
        y_col = st.selectbox("Select Y (Target)", [col for col in cols if col != x_col], key="ws_y")
        if st.button("Run Linear Regression 🚀", key="ws_regress"):
            X = data[[x_col]].values
            y = data[y_col].values
            model = LinearRegression().fit(X, y)
            y_pred = model.predict(X)
            r2 = model.score(X, y)
            # Visualize
            fig, ax = plt.subplots(figsize=(7,5))
            ax.scatter(X, y, c="#3066BE", alpha=0.6, label="Actual")
            ax.plot(X, y_pred, color="#F2A900", lw=3, label="Prediction")
            ax.set_facecolor("#e5e5e5")
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            ax.set_title("Wall Street Linear Regression", color="#13315C")
            ax.legend()
            st.pyplot(fig)
            st.success(f"R² Score: {r2:.3f}")
            st.info(f"Regression Equation: {y_col} = {model.coef_[0]:.2f} × {x_col} + {model.intercept_:.2f}")

        st.markdown("""
        <img src='https://media.giphy.com/media/3o6gE5aYpVJJ7n12re/giphy.gif' width='220'>
        <p>Wall Street never sleeps—neither does your data!</p>
        """, unsafe_allow_html=True)
