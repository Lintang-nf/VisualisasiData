import streamlit as st
import pandas as pd
import numpy as np
import graphviz as graphviz

st.title("graviz Chart")
st.write("Kelompok: 6")
st.markdown("""
1. Muhammad Faqih Jundullah - 0110121225
2. Lintang Kasyfi Ramadhan - 0110222194
""")

st.graphviz_chart("""
digraph {
    "training Data" -> "ML algorithm"
    "ML algorithm" -> "Model"
    "Model" -> "Results Forecasting"
    "New Data" -> "Model"   
}
""")