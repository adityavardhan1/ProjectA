import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

def load_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("structure.css")

st.markdown(
    """
    <div class="top-menu">
        <a href = "#"> HOME </a>
        <a href = "#"> ABOUT US </a>
        </div>
        """, unsafe_allow_html=True
        )



st.title("My Styled streamlit App")

st.sidebar.header("sidebar")
st.sidebar.button("click me")

st.markdown('<div class="main-content">', unsafe_allow_html=True)
st.write("welcome to my page")
st.markdown('</div>', unsafe_allow_html=True)