import streamlit as st
import matplotlib.pyplot as plt 
import pandas as pd

# Data dummy
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]

data = {
    'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'Penjualan_Cokelat': [50, 60, 70, 80, 90, 100, 110, 120, 130],
    'Penjualan_Vanila': [60, 70, 80, 90, 100, 110, 120, 130, 140],
    'Penjualan_Stroberi': [40, 50, 60, 70, 80, 90, 100, 110, 120],
    'Kelembapan': [60, 65, 70, 75, 80, 85, 90, 95, 100]
}

df = pd.DataFrame(data)

# Judul aplikasi
st.title('Visualisasi Hubungan Penjualan Es Krim dengan Suhu')
st.sidebar.header('Pengaturan visualisasi')

options = st.sidebar.selectbox(
    'Pilih contoh sactterplot:',
    ('Basic Scatter Plot', 
     'Kustomisasi Scatter Plot', 
     'Multiple Scatter Plot', 
     'Analisis Scatter Plot')
)

st.caption('Praktikum 5 - Visualisasi Data dengan Scatter Plot')
st.markdown("""
            - Lintang Kasyfi Ramadhan (0110222194)
            - Muhammad Faqih Jundullah (0110121225)
            """)







#                                                                               BASIC SCATTER PLOT
def basic_scatter():
    st.subheader('Basic Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color='blue')
    ax.set_title('Hubungan Penjualan Es Krim dan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    st.pyplot(fig)






#                                                                            KUSTOMISASI SCATTER PLOT
def kustom_scatter():
    st.subheader('Kustomisasi Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color='orange', s=100, edgecolor='black', alpha=0.7)
    ax.set_title('Hubungan Penjualan Es Krim dan Suhu (Kustom)')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    st.pyplot(fig)





#                                                                              MULTIPLE SCATTER PLOT
# Data tambahan untuk kategori hari
penjualan_kerja = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_akhir_pekan = [60, 70, 80, 100, 110, 120, 140, 160, 200]

# Multiple scatter plot
def multiple_scatter():
    st.subheader('Multiple Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan_kerja, color='green', label='Hari Kerja', s=80)
    ax.scatter(suhu, penjualan_akhir_pekan, color='purple', label='Akhir Pekan', s=80)
    ax.set_title('Penjualan Es Krim Berdasarkan Hari')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    st.pyplot(fig)




#                                                                              ANALISIS SCATTER PLOT
def scatter_3_variables():
    
    st.subheader('Analisis dengan Scatter Plot')
    jenis_es_krim = st.selectbox('Pilih Jenis Es Krim:', ['Cokelat', 'Vanila', 'Stroberi'])

    # Menentukan kolom penjualan berdasarkan pilihan
    if jenis_es_krim == 'Cokelat':
        penjualan = df['Penjualan_Cokelat']
    elif jenis_es_krim == 'Vanila':
        penjualan = df['Penjualan_Vanila']
    else:
        penjualan = df['Penjualan_Stroberi']

    # Tampilkan tabel data
    st.subheader('Data Penjualan dan Suhu')
    st.dataframe(df)

    # Membuat Scatter Plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(df['Suhu'], penjualan, c=df['Kelembapan'], s=100, cmap='coolwarm', alpha=0.7)

    ax.set_title(f'Hasil Penjualan {jenis_es_krim} vs Suhu dan Kelembapan')
    ax.set_xlabel('Suhu')
    ax.set_ylabel(f'Penjualan Es Krim {jenis_es_krim}')
    fig.colorbar(scatter, label='Kelembapan (%)')

    st.pyplot(fig)

    # Ringkasan hubungan
    st.subheader('Analisis Hubungan')
    st.write(f'Grafik menunjukkan hubungan antara suhu, kelembapan, dan penjualan es krim jenis **{jenis_es_krim}**.')

#scouting bedasarkan menu sidebar
if options == 'Basic Scatter Plot':
    basic_scatter()
elif options == 'Kustomisasi Scatter Plot':
    kustom_scatter()
elif options == 'Multiple Scatter Plot':
    multiple_scatter()
elif options == 'Analisis Scatter Plot':
    scatter_3_variables()