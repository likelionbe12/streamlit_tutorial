# main.py
import streamlit as st
import pandas as pd
import time
import numpy as np

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

_LOREM_IPSUM = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""


def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

    # yield pd.DataFrame(
    #     np.random.randn(5, 10),
    #     columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    # )

    # for word in _LOREM_IPSUM.split(" "):
    #     yield word + " "
    #     time.sleep(0.02)

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

if st.button("Stream data"):
    st.write_stream(stream_data)

import streamlit as st

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")
sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")