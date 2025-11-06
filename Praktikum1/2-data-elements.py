import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

st.title("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 1")
st.markdown("""
1. Muhammad Faqih Jundullah
2. Lintang Kasyfi            
""")

st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.rand(30,10),
    columns=('col_no %d' % i for i in range(10))
)

st.dataframe(df)

st.subheader("Highlight Minimum Value di Dataframe")

st.dataframe(df.style.highlight_min(axis=0))

st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.rand(30,10),
    columns=('col_no %d' % i for i in range(10))
)
st.table(df)

st.subheader("Metrics")
st.metric(label="Temprature", value="31 oC", delta="1.2 oc")

col1, col2, col3 = st.columns(3)

col1.metric("Curah Hujan", "100 cm", "10 cm")
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar", delta_color="inverse")
col3.metric(label="Pelanggan", value=100, delta=10, delta_color="off")

st.metric(label="speed", value=None, delta=0)
st.metric("Tress", "91456", "-1132649")

df = pd.DataFrame(
    np.random.rand(30, 10),
columns=('col_no %d' % i for i in range(10)))
st.write('Here is our Data', df, 'Data is in dataframe format.\n', "\nWrite is Super function")

df = pd.DataFrame(
np.random.randn(10, 2),
columns=['a', 'b'])
chart = alt.Chart(df).mark_bar().encode(
x='a', y='b', tooltip=['a', 'b'])
st.write(chart)

"Adding 5 & 4 =", 5+4
a = 5
'a', a
"""
# Magic Feature
Markdown working without defining its function explicity.
"""
df = pd.DataFrame({'col': [1,2]})
'dataframe', df

s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
"chart", chart