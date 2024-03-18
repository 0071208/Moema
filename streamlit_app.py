import streamlit as st
import pandas as pd
voc=pd.read_CSV('https://docs.google.com/spreadsheets/d/1jH6kJJISFA0Ye4gE4CzG7ZEjBJhCRelGOZN-HnxyZBQ/edit?pli=1#gid=0')
st.dataframe(voc)
