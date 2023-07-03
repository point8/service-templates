import numpy as np
import pandas as pd
import streamlit as st

st.write("# Look at this data\n It's *awesome*!")

df = pd.DataFrame(np.random.normal(size=100))

st.line_chart(df)
