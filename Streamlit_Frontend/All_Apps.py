import streamlit as st

st.set_page_config(page_title="Rasamrit Health",
                  page_icon='../Assets/logo.jpg',)

st.write('# Welcome to :green[Rasamrit] Diet Recommendation System! 🥗')

st.sidebar.success("Select a recommendation app.")
#st.sidebar.image('../Assets/logo.jpg')

st.markdown(
    """
    A Diet Recommendation Assistant powered by AI
    """
)

st.image('../Assets/logo.jpg')