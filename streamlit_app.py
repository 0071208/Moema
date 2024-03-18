import streamlit as st
import pandas as pd
voc=pd.read_CSV('https://docs.google.com/spreadsheets/d/e/2PACX-1vQLTze3TEoe78fBV0iekeHnumxiW8kWW33WjqhK65kKxll8HFbZFUGUqBwLBbdK8JZD4-z9uiOe7Bb_/pub?output=csv')
st.dataframe(voc)
