import streamlit as st

from iris_navigation import ABOUT_PAGE, PREDICTION_PAGE, VISUALIZATIONS_PAGE


st.set_page_config(page_title="Iris Flower Explorer", page_icon="🌸", layout="wide")

navigation = st.navigation(
    [ABOUT_PAGE, VISUALIZATIONS_PAGE, PREDICTION_PAGE],
    position="hidden",
)
navigation.run()
