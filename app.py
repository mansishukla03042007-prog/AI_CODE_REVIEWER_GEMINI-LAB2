import streamlit as st
from utils import header
from code_reviewer import review_code

st.set_page_config(page_title="AI Code Reviewer", page_icon=" ",layout="wide")
header()

languages=st.selectbox("Programming Language",["Python","Java","JavaScript","C"])
review_type=st.radio("Review Type",["Basic","Detailed","Security"])
temperatures =st.slider("Temperature",0.0,1.0,0.2,0.1)
code=st.text_area("Paste Your Code",height=300)

if st.button("Review Code",use_container_width=True):
    if not code.strip():
        st.warning("Please paste from code.")
    else:
        with st.spinner("Reviewing"):
            result=review_code(languages, review_type, code, temperatures)
        st.markdown(result)

