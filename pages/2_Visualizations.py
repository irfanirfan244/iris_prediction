import numpy as np
import pandas as pd
import streamlit as st

from iris_data import dataset, feature_names, species_names
from iris_navigation import show_page_navigation


show_page_navigation("visualizations")
st.title("Explore Iris measurements")

selected_species = st.multiselect(
    "Species to include",
    options=species_names,
    default=species_names,
)
filtered_dataset = dataset[dataset["species"].isin(selected_species)]

if filtered_dataset.empty:
    st.info("Select at least one species to display the visualizations.")
else:
    first_column, second_column = st.columns(2)
    with first_column:
        x_feature = st.selectbox("Horizontal axis", feature_names, index=2)
    with second_column:
        y_feature = st.selectbox("Vertical axis", feature_names, index=3)

    st.subheader("Compare two measurements")
    st.scatter_chart(
        filtered_dataset,
        x=x_feature,
        y=y_feature,
        color="species",
        width="stretch",
    )
    st.caption(
        "Each point represents one flower. The color indicates its species; "
        "the axes show the selected measurements in centimeters."
    )

    measurement = st.selectbox(
        "Measurement distribution",
        feature_names,
        key="distribution_feature",
    )
    histogram_rows = []
    bin_edges = np.histogram_bin_edges(dataset[measurement], bins=10)
    for species in selected_species:
        values = dataset.loc[dataset["species"] == species, measurement]
        counts, _ = np.histogram(values, bins=bin_edges)
        for index, count in enumerate(counts):
            histogram_rows.append(
                {
                    "Range (cm)": (
                        f"{bin_edges[index]:.1f}–{bin_edges[index + 1]:.1f}"
                    ),
                    "Species": species,
                    "Flowers": int(count),
                }
            )

    st.subheader(f"Distribution of {measurement}")
    st.bar_chart(
        pd.DataFrame(histogram_rows),
        x="Range (cm)",
        y="Flowers",
        color="Species",
        width="stretch",
    )

    st.subheader("Summary statistics")
    st.dataframe(
        filtered_dataset.groupby("species", observed=True)[feature_names]
        .agg(["mean", "min", "max"])
        .round(2),
        width="stretch",
    )
