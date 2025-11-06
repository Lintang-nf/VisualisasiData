# import libary yang dibutuhkan
import streamlit as st

# text element
# header - untuk membuat tulisan header
st.header("Ini header")
st.subheader("ini sub header")
st.text("ini teks biasa tanpa format")
st.markdown("ini teks bold dan ini teks italic")
st.markdown("""
- ini baris 1 
- ini menggunakan markdown multibaris
1. ini baris 2
2. ini menggunakan markdown multibaris
* ini baris 3
* ini menggunakan markdown multibaris                        
""")
st.caption("ini caption")
st.title("Ini Judul")

# coba mandiri
st.title("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 1 : Teks Element")
st.markdown("""
1. Muhammad Faqih Jundullah
2. Lintang Kasyfi Ramadhan            
""")

# Bagian 2
st.header("Display LaTeX")
st.latex(r""" (a+b)^2 = a^2 + b^2 + 2ab """)

# Bagian 3
st.header("Display Code")
st.subheader("Python Code")

code = '''
def hello():
    print("Hello, Streamlit!)
'''

st.code(code, language='python')

st.subheader("Java Code")
st.code("""
    public class GFG{
        public static void main (String arg []){
            System.out.printIn("Hello World!");
            }
        }
""", language='java')

st.subheader("JavaScript Code")
st.code("""
<p id="demo"></p>
<script>
try {
        addlert("Welcome guest!); //kesalahan ketik (addlaert)
        sengaja dibuat untuk menimbulkan error
        }
catch(err){
        document.getElementById("demo").innerHTML = err.massage; //menampilkan pesan error di elemen html dengan id 'demo'
        }
        </script>        
""", language='javascript')