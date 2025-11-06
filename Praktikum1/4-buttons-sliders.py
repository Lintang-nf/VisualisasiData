import time
import streamlit as st
import pandas as pd
import numpy as np


st.write("Kelompok: 6")
st.markdown("""
1. Muhammad Faqih Jundullah - 0110121225
2. Lintang Kasyfi Ramadhan - 0110222194
""")

# Defining a Button
st.title("Creating a button")

button = st.button('Click Here')

if button:
    st.write('You have clicked the Button')
else:
    st.write('You have not clicked the Button')

# Defining Radio Button
st.title('Creating Radio Buttons')

gender = st.radio(
    "Select your gender",
    ('Male', 'Female', 'Others')
)

if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write('You have selected Female.')
else:
    st.write('You have selected Others.')


# Defining Checkboxes
st.title('Creating Checkboxes')
st.write('Select your Hobbies:')

check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

# Creating Dropdown
st.title('Creating Dropdown')

hobby = st.selectbox('Choose your hobby: ', 
                     ('Books', 'Movies', 'Sports'))


# Defining Multi Select with Pre-Selection
st.title('Multi-Select')

hobbies = st.multiselect(
    'What are your Hobbies:',
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
    ['Reading', 'Playing']
)

# Creating Download Button
st.title("Download Button")

down_btn = st.download_button(
    label="Download Image",
    data=open("c:/elstriper.png", "rb"),
    file_name="4 penguin.png",
    mime="image/jpg"
)

# Defining Progress Bar
st.title('Progress Bar')

download = st.progress(0)

for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage + 1)

st.write('Download Complete')


# Defining Spinner
st.title("Spinner")

with st.spinner('Loading...'):
    time.sleep(5)

st.write('Hello Data Scientists')