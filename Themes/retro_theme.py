import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from utils import load_kaggle_data, fetch_yahoo_data, retro_theme_style

def show_retro_theme():
    retro_theme_style()
    st.markdown("""
        <h2>🕹️ Retro 80s Theme: Logistic Regression</h2>
        <img src="https://media.giphy.com/media/3o7qE1YN7aBOFPRw8E/giphy.gif" width="320">
        <p style="font-family: 'Press Start 2P',monospace; font-size:16px;">
        Welcome to the neon-soaked 80s—where finance meets arcade fun! Try some ML with synthwave style.
        </p>
    """, unsafe_allow_html=True)

    st.header("Step 1: Load Data (Kaggle or Yahoo Finance)", divider='rainbow')
    data_source = st.radio(
        "Select data source",
        ["Upload Kaggle CSV", "Fetch from Yahoo Finance"],
        index=0
    )

    data = None
    if data_source == "Upload Kaggle CSV":
        file = st.file_uploader("Choose a CSV file", type="csv")
        if file is not None:
            data = load_kaggle_data()
            if data is not None:
                st.session_state["retro_data"] = data
    else:
        data = fetch_yahoo_data()
        if data is not None:
            st.session_state["retro_data"] = data

    data = st.session_state.get("retro_data", None)

    if data is not None:
        st.success("Data loaded! Let's get pixelated.")
        st.write(data.head(10))
        st.header("Step 2: Logistic Regression (Binary Classification)", divider='rainbow')
        cols = data.select_dtypes(include=np.number).columns.tolist()
        if len(cols) < 2:
            st.error("Need at least two numeric columns for logistic regression.")
            return
        x_col = st.selectbox("Select Feature (X)", cols, key="retro_x")
        y_col = st.selectbox("Select Target (Y)", [col for col in cols if col != x_col], key="retro_y")
        y = data[y_col].values
        unique_vals = np.unique(y)

        # If not binary, offer to binarize with median split
        binarize = False
        if len(unique_vals) != 2:
            st.info(f"'{y_col}' is not binary. To use it for classification, you can binarize it using the median value.")
            binarize = st.checkbox(f"Binarize '{y_col}' (1 if above median, 0 otherwise)")
            if binarize:
                median_val = np.median(y)
                y_bin = (y > median_val).astype(int)
                st.success(f"Binarized '{y_col}': 1 if value > {median_val:.2f}, 0 otherwise.")
            else:
                st.warning("Please binarize the column or select a naturally binary target for logistic regression.")
                return
        else:
            y_bin = y

        if st.button("Run Logistic Regression 🎯", key="retro_logreg"):
            X = data[[x_col]].values
            if len(np.unique(y_bin)) != 2:
                st.error("Target (Y) must be binary. Please binarize or select a suitable column.")
                return
            clf = LogisticRegression().fit(X, y_bin)
            y_pred = clf.predict(X)
            acc = clf.score(X, y_bin)
            fig, ax = plt.subplots(figsize=(7,5))
            ax.scatter(X, y_bin, color="#ff00cc", label="Actual", alpha=0.7)
            ax.scatter(X, y_pred, color="#00ffe7", marker="x", label="Predicted", alpha=0.6)
            ax.set_xlabel(x_col)
            ax.set_ylabel(f"{y_col} (binary)")
            ax.set_title("Retro Logistic Regression", color="#00ffe7")
            ax.legend()
            st.pyplot(fig)
            st.success(f"Accuracy: {acc:.3f}")
            st.info("Try classifying: will the market boom or bust, retro style?")

        st.markdown("""
        <img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" width="200">
        <p>Neon data, analog logic!</p>
        """, unsafe_allow_html=True)
    else:
        st.info("Please upload a dataset or fetch Yahoo Finance data to proceed.")
