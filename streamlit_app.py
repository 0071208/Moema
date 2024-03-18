import streamlit as st
import pandas as pd
voc=pd.read_CSV('lien')
st.dataframe(voc)
