import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from nltk.stem import *

st.header('Stemming Example')


text = st.text_input('Give a Text: ', '')

stemmer = PorterStemmer()

words = text.split()


stemmed_words = [stemmer.stem(word) for word in words] 



df = pd.DataFrame({
     'Words': words,
     'Stemmer Words': stemmed_words
     })

st.write(df)


