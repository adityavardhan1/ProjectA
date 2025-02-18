import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

def load_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("structure.css")


st.markdown("""
    <style>
        /* Hide the Deploy button */
        header [data-testid="stDeployButton"] {
            display: none !important;
        }
        
        /* Hide Streamlit footer */
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .top-right-menu {
            position: absolute;
            top: 10px;
            right: 20px;
            z-index: 1000;
            background-color: #f8f9fa;
            padding: 10px;
            border-radius: 10px;
        }
        .top-right-menu a {
            margin: 0 15px;
            text-decoration: none;
            font-weight: bold;
            color: #007bff;
            font-size: 16px;
        }
        .top-right-menu a:hover {
            color: #0056b3;
        }
    </style>
""", unsafe_allow_html=True)

# Creating the top-right menu using HTML
menu_html = """
    <div class="top-right-menu">
        <a >Home</a>
        <a >About</a>
        <a >Contact</a>
        <a >Subscribe</a>
    </div>
"""
st.markdown(menu_html, unsafe_allow_html=True)



st.title("My Styled streamlit App")

st.sidebar.header("sidebar")
st.sidebar.button("click me")

st.markdown('<div class="main-content">', unsafe_allow_html=True)
st.write("welcome to my page")
st.markdown('</div>', unsafe_allow_html=True)