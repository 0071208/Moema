import streamlit as st
import pandas as pd
import numpy as np
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQLTze3TEoe78fBV0iekeHnumxiW8kWW33WjqhK65kKxll8HFbZFUGUqBwLBbdK8JZD4-z9uiOe7Bb_/pub?output=csv')
l=voc.shape[0]
i=np.random.choice(range(l))
word_fr=voc['Définition'].values[i]
word_chi=voc['Hanzi'].values[i]
st.write(word_fr+" "+word_chi)
st.button("refresh")
st.write(indices)
indices=np.random.choice(l,size=4,replace=false)
j=np.random.choice(indices)

word_fr=voc["Définition"].values[j]
st.write("Traduis: "+word_fr)
for i in range(4)
st.button(voc["Hanzi"].values[indices[i]],on_click=is_correct,args((indices[i],j))
def is_correct(i,j):
  if i==j:
    st.write("Bravooo")
  else:
    st.write("Raté!")
