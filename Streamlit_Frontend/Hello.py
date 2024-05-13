import streamlit as st

st.set_page_config(page_title="Rasamrit Health",
                  page_icon='../Assets/logo.jpg',)


st.write("# Welcome to Rasamrit's Diet Recommendation System! 🥗")

st.sidebar.success("Select a recommendation app.")
st.sidebar.image('../Assets/logo.jpg')

st.markdown(
    """
    A diet recommendation web application using content-based approach with Scikit-Learn.
    """
)
