import streamlit as st
from pages.utilities.cdlt_scraper import *
        

st.title("Documentation Checker")

# Create a form for user input

insurance_company = st.selectbox(
    'Select Insurance Company',
    ('Anthem',)
)
cpt_code = st.text_input(label='Enter CPT Code')

if st.button('Submit'):
    run_scraper('Commercial', 'NY', cpt_code)





