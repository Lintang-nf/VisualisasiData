import streamlit as st
import pandas as pd
import numpy as np

st.title("Map")
st.write("Kelompok: 6")
st.markdown("""
1. Muhammad Faqih Jundullah - 0110121225
2. Lintang Kasyfi Ramadhan - 0110222194
""")

locate_map =pd.DataFrame(
    np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
columns = ['latitude', 'longitude'])
st.map(locate_map)