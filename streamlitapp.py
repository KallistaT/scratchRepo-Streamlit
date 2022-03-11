# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 12:38:43 2022

@author: kalt9
"""

import streamlit as st
import pandas as pd
import numpy as np
import time

# Loading in csvs
@st.cache
def load_hospitals():
    hospital_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_hospital_2.csv')
    return hospital_df

@st.cache
def load_inpatient():
    inpatient_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')
    return inpatient_df

@st.cache
def load_outpatient():
    outpatient_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')
    return outpatient_df

# Loading bar
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)
    
## Streamlit Questions
st.title('HHA 507 Final Assignment: E2E with Streamlit')
st.subheader('Kallista Tong')
st.write('Questions:')
st.write('1. How does Stony Brook Hospital''s rating compare with the rest of NY?')
st.write('2. What is the most expensive inpatient DRGs for Stony Brook?')
st.write('3. What is the most expensive outpatient APCs for Stony Brook?')
st.write('4. ...')
st.write('5. ...')
st.write('6. ...')    

# Loading in dataframes
hospital_df = load_hospitals()
inpatient_df = load_inpatient()
outpatient_df = load_outpatient()

# Previewing dataframes
st.header('Hospital Data Preview')
st.markdown('This dataset displays information on hospitals across the United States.')
st.dataframe(hospital_df)

st.header('Inpatient Data Preview')
st.markdown('This dataset displays information on inpatient data for Stony Brook University Hospital.')
st.dataframe(outpatient_df)

st.header('Outpatient Data Preview')
st.markdown('This dataset displays information on outpatient data for Stony Brook University Hospital.')
st.dataframe(inpatient_df)

# Creating a dataframe for New York State hospitals
ny_df = hospital_df[hospital_df['state'] == 'NY']
st.header('Hospitals in New York State')
st.markdown('This dataset displays information on hospitals in New York State.')
st.dataframe(ny_df)

# Creating a dataframe for Stony Brook University Hospital
sbu_df = hospital_df[hospital_df['hospital_name'] == 'SUNY/STONY BROOK UNIVERSITY HOSPITAL']
st.header('Stony Brook University Hospital')
st. markdown('This dataset displays information on Stony Brook University Hospital')
st.dataframe(sbu_df)


