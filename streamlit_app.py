import streamlit as st
import pandas as pd
import numpy as np
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQLTze3TEoe78fBV0iekeHnumxiW8kWW33WjqhK65kKxll8HFbZFUGUqBwLBbdK8JZD4-z9uiOe7Bb_/pub?output=csv')
st.dataframe(voc)
l=voc.shape[0]
i=np.random.choice(range(l))
word_fr=voc['Définition'].values[i]
word_chi=voc['hanzi'].values[i]
st.write(word_fr+"hanzi"+word_chi)
