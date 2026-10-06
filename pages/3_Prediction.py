import pandas as pd
import streamlit as st

from iris_data import dataset, feature_names, load_model, species_names
from iris_navigation import show_page_navigation


show_page_navigation("prediction")
st.title("Predict an Iris species")
st.write(
    "Adjust the four flower measurements, then ask the trained model to predict "
    "which Iris species they most resemble."
)

controls = st.columns(4)
measurements = []
for index, (column, feature) in enumerate(zip(controls, feature_names)):
    minimum = float(dataset[feature].min())
    maximum = float(dataset[feature].max())
    default = float(dataset[feature].mean())
    measurements.append(
        column.slider(
            feature.replace(" (cm)", "").title() + " (cm)",
            min_value=minimum,
            max_value=maximum,
            value=default,
            step=0.1,
            key=f"measurement_{index}",
        )
    )

if st.button("Predict species", type="primary"):
    model = load_model()
    input_data = pd.DataFrame([measurements], columns=feature_names)
    prediction = model.predict(input_data)[0]
    predicted_species = species_names[int(prediction)]

    st.success(f"Predicted species: **{predicted_species.title()}**")
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(input_data)[0]
        probability_data = pd.DataFrame(
            {
                "Species": [
                    species_names[int(class_index)]
                    for class_index in model.classes_
                ],
                "Probability": probabilities,
            }
        ).sort_values("Probability", ascending=False)
        st.subheader("Model confidence")
        st.bar_chart(
            probability_data,
            x="Species",
            y="Probability",
            width="stretch",
        )
