import streamlit as st


ABOUT_PAGE = st.Page(
    "pages/1_About.py",
    title="About the dataset",
    icon="📘",
    default=True,
)
VISUALIZATIONS_PAGE = st.Page(
    "pages/2_Visualizations.py",
    title="Visualizations",
    icon="📊",
)
PREDICTION_PAGE = st.Page(
    "pages/3_Prediction.py",
    title="Prediction",
    icon="🔎",
)


def show_page_navigation(current_page: str) -> None:
    pages = [
        ("about", ABOUT_PAGE, "About the dataset"),
        ("visualizations", VISUALIZATIONS_PAGE, "Visualizations"),
        ("prediction", PREDICTION_PAGE, "Prediction"),
    ]
    columns = st.columns(len(pages))
    for column, (page_id, page, label) in zip(columns, pages):
        with column:
            st.page_link(
                page,
                label=label,
                disabled=page_id == current_page,
                use_container_width=True,
            )
    st.divider()
