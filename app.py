import streamlit as st
import pandas as pd
import os
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.header("CLEAN-DIT")

file = st.file_uploader("Upload the file you want to clean")

try:
    
    ext = os.path.splitext(file.name)[-1].lower()
    if file is not None:
        
        if ext == '.csv':
            df = pd.read_csv(file)
        elif ext == '.xlsx':
            df = pd.read_excel(file)
        else:
            st.error("File is not a CSV or EXCEL file")
            
    report_generate = st.checkbox("Generate Report")
       
    if report_generate:
        
        pr = df.profile_report()

        st_profile_report(pr)
        
    st.subheader("Cleaning Actions")

    st.write(" ")

    if st.button("DROP NULLs"):
        df_clean = df.copy()
        df_clean.dropna(inplace = True)
        df_clean = df_clean.to_csv(index= False).encode('utf-8')
        
        st.download_button(
        label="Download data as CSV",
        data=df_clean,
        file_name='clean.csv',
        mime='text/csv',)
        
    if st.button("DROP Duplicates"):
        df_clean = df.copy()
        df_clean.drop_duplicates(inplace = True)
        df_clean = df_clean.to_csv(index= False).encode('utf-8')
        
        st.download_button(
        label="Download data as CSV",
        data=df_clean,
        file_name='clean.csv',
        mime='text/csv',)
        
except AttributeError:
    st.write("Please Upload A Dataset to Continue")

        
