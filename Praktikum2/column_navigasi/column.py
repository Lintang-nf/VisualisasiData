import streamlit as st
import pandas as pd
import numpy as np

st.title("Column")
st.write("Kelompok: 6")
st.markdown("""
1. Muhammad Faqih Jundullah - 0110121225
2. Lintang Kasyfi Ramadhan - 0110222194
""")

col1, col2= st.columns(2)

col1.write("Ini adalah kolom pertama")
col1.image("../../Praktikum1/assets/mybini.png")
col2.write("Ini adalah kolom kedua")