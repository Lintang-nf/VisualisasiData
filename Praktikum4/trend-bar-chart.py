import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Bar Chart")
st.write("Kelompok 6:")
st.markdown("""
            - Lintang Kasyfi Ramadhan (0110222194)
            - Muhammad Faqih Jundullah (110121225)
            """)

# Data jumlah mahasiswa per jurusan selama 5 tahun
data = {
    'Tahun': ['2019', '2020', '2021', '2022', '2023'],
    'Ilmu Komputer': [100, 110, 120, 130, 140],
    'Sistem Informasi': [120, 125, 135, 145, 160],
    'Teknik Informatika': [90, 95, 100, 105, 110],
    'Data Science': [70, 75, 80, 85, 90]
}

# Membuat dataframe untuk visualisasi
df = pd.DataFrame(data)

# Judul aplikasi Streamlit
st.title("Visualisasi Tren Jumlah Mahasiswa Memilih Jurusan Komputer (5 Tahun Terakhir)")

# Filter tahun (multi-select)
filter_tahun = st.multiselect("Pilih Tahun:", df['Tahun'], default=df['Tahun'])

# Daftar jurusan
jurusan_list = ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science']
filter_jurusan = st.multiselect("Pilih Jurusan:", jurusan_list, default=jurusan_list)

# Filter data berdasarkan pilihan pengguna
filtered_data = df[df['Tahun'].isin(filter_tahun)][['Tahun'] + filter_jurusan]

# Menampilkan tabel data yang sudah difilter
st.subheader("Data Jumlah Mahasiswa")
st.dataframe(filtered_data)

# Membuat Bar Chart dengan filter
st.subheader("Bar Chart dengan Filter")
fig, ax = plt.subplots(figsize=(10, 6))

x = range(len(filtered_data['Tahun']))  # Posisi tahun di sumbu X
width = 0.2  # Lebar setiap bar

# Membuat bar untuk setiap jurusan yang dipilih
for i, jur in enumerate(filter_jurusan):
    ax.bar([p + i * width for p in x], filtered_data[jur], width=width, label=jur)

# Menyesuaikan label sumbu X (tahun) agar berada di tengah-tengah kelompok bar
ax.set_xticks([p + width * (len(filter_jurusan) - 1) / 2 for p in x])
ax.set_xticklabels(filtered_data['Tahun'])

# Judul dan label
ax.set_title("Jumlah Mahasiswa per Jurusan (Berdasarkan Filter)")
ax.set_xlabel("Tahun")
ax.set_ylabel("Jumlah Mahasiswa")
ax.legend()

# Menampilkan plot di Streamlit
st.pyplot(fig)