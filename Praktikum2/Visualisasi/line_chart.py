import streamlit as st
import pandas as pd
import numpy as np

st.title("Line Chart")
st.write("Kelompok: 6")
st.markdown("""
1. Muhammad Faqih Jundullah - 0110121225
2. Lintang Kasyfi Ramadhan - 0110222194
""")

df = pd.DataFrame(
    np.random.rand(40, 4),
    columns=['C1', 'C2', 'C3', 'C4']
)

st.line_chart(df)