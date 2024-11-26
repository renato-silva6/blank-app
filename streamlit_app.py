import streamlit as st

st.header("🎈 My new app")
st.subheader("This is my subtitle")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.button("Click me")
st.checkbox("I agree")
st.pills("Tags", ["Sports", "Politics"])
st.radio("Pick one", ["cats", "dogs"])
