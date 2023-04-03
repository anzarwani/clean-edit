import streamlit as st
import pandas as pd
import os

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
            
    raw_file = st.checkbox("Show Data")
    null_values = st.checkbox("Analyze")

    if raw_file:
        st.write(df)
        
    if null_values:
        null_value_percent = df.isnull().sum() / df.shape[0] * 100
        st.markdown("**Percentage of NULL Values**")
        st.write(null_value_percent)
        
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
        
except AttributeError:
    st.write("Please Upload A Dataset to Continue")

        
