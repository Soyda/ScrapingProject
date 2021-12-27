import streamlit as st
import pandas as pd
import numpy as np

animal_df = pd.read_json('not_really_clean_animals.json')

st.title("Animals")
st.write(animal_df)