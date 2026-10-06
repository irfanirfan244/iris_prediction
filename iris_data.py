from pathlib import Path
import pickle

import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris


iris = load_iris()
feature_names = list(iris.feature_names)
species_names = list(iris.target_names)
dataset = pd.DataFrame(iris.data, columns=feature_names)
dataset["species"] = pd.Categorical.from_codes(iris.target, species_names)


@st.cache_resource
def load_model():
    model_path = Path(__file__).with_name("iris_model.pkl")
    with model_path.open("rb") as model_file:
        return pickle.load(model_file)
