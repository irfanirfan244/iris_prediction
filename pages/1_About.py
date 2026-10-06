import streamlit as st

from iris_data import dataset, feature_names, species_names
from iris_navigation import show_page_navigation


show_page_navigation("about")

st.title("🌸 Iris Flower Explorer")
st.caption("An introduction to the Iris dataset and its flower measurements.")

st.header("Getting to know the Iris dataset")
st.write(
    "The Iris dataset is a classic collection of flower measurements used to "
    "explore data analysis and classification. It contains 150 flowers: 50 "
    "each from *Iris setosa*, *Iris versicolor*, and *Iris virginica*."
)

metric_columns = st.columns(4)
metric_columns[0].metric("Flowers", len(dataset))
metric_columns[1].metric("Species", len(species_names))
metric_columns[2].metric("Measurements per flower", len(feature_names))
metric_columns[3].metric("Measurement unit", "cm")

st.subheader("What do the measurements mean?")
st.write(
    "Each flower is described by four measurements, all recorded in centimeters. "
    "A **sepal** is one of the outer, leaf-like parts that protects a flower bud. "
    "A **petal** is one of the inner flower parts, often colorful."
)
st.table(
    [
        {
            "Measurement": feature,
            "What it measures": description,
            "Typical range in this dataset (cm)": (
                f"{dataset[feature].min():.1f}–{dataset[feature].max():.1f}"
            ),
        }
        for feature, description in zip(
            feature_names,
            [
                "The length of one outer sepal, from base to tip.",
                "The width of one outer sepal at its widest point.",
                "The length of one inner petal, from base to tip.",
                "The width of one inner petal at its widest point.",
            ],
        )
    ]
)

st.subheader("The three species")
st.write(
    "- **Setosa** — generally has shorter petals than the other two species.\n"
    "- **Versicolor** — typically falls between setosa and virginica in petal size.\n"
    "- **Virginica** — often has the largest petals in this dataset."
)
with st.expander("Preview the data"):
    st.dataframe(dataset, width="stretch", hide_index=True)
