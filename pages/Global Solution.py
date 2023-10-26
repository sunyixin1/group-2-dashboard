import streamlit as st

# title
st.title("Global solution")

# show HTMLfile
html_file_path = "graph/map111.html"
with open(html_file_path, 'r', encoding='utf-8') as f:
    html_content = f.read()
    st.components.v1.html(html_content, width=800, height=600)
