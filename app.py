
import streamlit as st
import pandas as pd
import numpy as np
import requests
import base64


def _max_width_():
    max_width_str = f"max-width: 1100px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True, 
    )

_max_width_()


st.title("🌐 HTML Table Scraper 🕸️")
st.markdown(" A simple HTML table scraper made in Python 🐍 & the amazing [Streamlit!](https://www.streamlit.io/) ")

st.markdown('### **1️⃣ Enter a URL to scrape **')

try:

    url =  st.text_input("", value='https://stackexchange.com/leagues/1/alltime/stackoverflow', max_chars=None, key=None, type='default')

    if url:
        
        arr = ['https://', 'http://']
        if any(c in url for c in arr):


    #    if "https" in url:

            header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }

            @st.cache(persist=True, show_spinner=False)
            def load_data():
                r = requests.get(url, headers=header)
                return pd.read_html(r.text)

            df = load_data()

            length = len(df)
            
            if length == 1:
                st.write("This webpage contains 1 table" )
            else: st.write("This webpage contains " + str(length) + " tables" )

            
            #st.write("This webpage contains " + str(length) + " tables" )

            if st.button("Show scraped tables"):
                st.table(df)
            else: st.empty()

            def createList(r1, r2): 
                return [item for item in range(r1, r2+1)] 
                
            r1, r2 = 1, length
            funct = createList(r1, r2)

            ###### Selectbox - Selectbox - Selectbox - Selectbox - Selectbox - Selectbox - Selectbox - 

            st.markdown('### **2️⃣ Select a table to export **')
            
            ValueSelected = st.selectbox('', funct)
            st.write('You selected table #', ValueSelected)


            df1 = df[ValueSelected -1]


            if df1.empty:

                st.warning ('ℹ️ - This DataFrame is empty!')

            
            else:
                
                #df1.index = df1.index.map(str)
                df1 = df1.replace(np.nan, 'empty cell', regex=True)
                #df1 = df1.replace('vte','')
                #df1.columns = df1.columns.str.replace(r'vte','')
                st.dataframe(df1)
                
            #df.columns = df.columns.str.replace(r"[()]", "_
            #df2 = df1.val.replace({'vte':'test'}, regex=True)
        else:
            st.error ('⚠️ - URL needs to be in a valid format, starting with *https://* or *http://*')
            
    else:
        
        st.warning ('ℹ️ - Paste a URL in the field above')
    
except ValueError:
    st.info ("ℹ️ - No table(s) to scrape on this page! 😊")

try:
    
    csv = df1.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    st.markdown('### ** ⬇️ Download the selected table to CSV **')
    href = f'<a href="data:file/csv;base64,{b64}" download="filtered_table.csv">** Click here to get your prize! 🎉**</a>'
    st.markdown(href, unsafe_allow_html=True)

except NameError:
    print ('wait')

st.markdown("---")

st.markdown('*Made with* :heart: * by [@DataChaz ](https://twitter.com/DataChaz)* [![this is an image link](https://i.imgur.com/Ltgzb7Y.png)](https://www.buymeacoffee.com/cwar05)')

