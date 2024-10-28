# main.py
import streamlit as st
import pandas as pd

st.title('My First App :confounded:')

msg = "hello world"
st.write(1234)
st.write(
    pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )
)

msg