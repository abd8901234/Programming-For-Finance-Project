# pixel_quest.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import base64

# -------------------------------
# 🎮 Pixel Quest Theme Styling
# -------------------------------

PIXEL_CSS = """
<style>
body {
    background-color: #fef6e4;
    color: #001858;
    font-family: 'Press Start 2P', cursive;
}
h1, h2, h3 {
    color: #ff6f61;
    text-shadow: 1px 1px 0 #ffbf69;
}
.stButton>button {
    background-color: #ff6f61;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px;
    font-size: 12px;
}
.stSelectbox, .stFileUploader, .stNumberInput, .stTextInput {
    background-color: #fff1e6;
}
</style>
"""

def set_pixel_background():
    st.markdown(PIXEL_CSS, unsafe_allow_html=True)
    pixel_gif = "https://media.giphy.com/media/XbZ5IYazY9c5e/giphy.gif"
    st.image(pixel_gif, use_column_width=True)

# -------------------------------
# 🚀 Main App Logic
# -------------------------------

def run_pixel_quest_theme():
    set_pixel_background()

    st.title("🎮 Pixel Quest Realm")
    st.subheader("🌟 Decision Tree Classification on Financial Data")

    # File upload
    uploaded_file = st.file_uploader("Upload your Kragle CSV financial dataset", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("✅ Dataset loaded successfully!")
        st.dataframe(df.head())

        # Target selection
        target = st.selectbox("🎯 Select target column for classification", df.columns)

        # Feature selection
        features = st.multiselect("🧠 Select feature columns", [col for col in df.columns if col != target])

        if features and target:
            # Split data
            X = df[features]
            y = df[target]

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Model training
            clf = DecisionTreeClassifier(max_depth=5, random_state=0)
            clf.fit(X_train, y_train)

            y_pred = clf.predict(X_test)

            # Accuracy
            accuracy = accuracy_score(y_test, y_pred)
            st.metric("📊 Accuracy", f"{accuracy * 100:.2f}%")

            # Classification Report
            st.text("📝 Classification Report")
            st.code(classification_report(y_test, y_pred))

            # Plot tree
            st.subheader("🌲 Visualized Decision Tree")
            fig, ax = plt.subplots(figsize=(12, 6))
            plot_tree(clf, feature_names=features, class_names=clf.classes_.astype(str), filled=True, ax=ax)
            st.pyplot(fig)

            # Feature importance
            st.subheader("🔥 Feature Importance")
            importance_df = pd.DataFrame({
                "Feature": features,
                "Importance": clf.feature_importances_
            }).sort_values(by="Importance", ascending=False)

            fig_imp = px.bar(importance_df, x="Feature", y="Importance", color="Importance",
                             color_continuous_scale="sunset", title="Feature Importance")
            st.plotly_chart(fig_imp, use_container_width=True)

        else:
            st.warning("⚠️ Please select both target and features to continue.")
    else:
        st.info("📂 Upload a CSV file to begin your pixelated adventure!")
