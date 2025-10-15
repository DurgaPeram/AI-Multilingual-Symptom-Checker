import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
STYLES = BASE_DIR / "styles"
STATIC = BASE_DIR / "static"
st.markdown(f"<style>{(STYLES/'base.css').read_text()}</style>", unsafe_allow_html=True)
# Header
col1, col2, col3 = st.columns([1, 7, 1])
with col1:
    st.image(str(STATIC/"images/icon.png"), width=130)
with col2:
    st.markdown("<h1 style='color:#1976d2; font-size:2.4rem;'>WELCOME TO MULTILINGUAL SYMPTOM CHECKER</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#333; text-align: center;'>Get Preliminary Health Guidance based on your Symptoms in your preferred language</p>", unsafe_allow_html=True)
with col3:
    st.image(str(STATIC/"images/medical.jpg"), width=130)


st.markdown("### How to Use")
st.markdown("""
<div class='card'>
1. Enter up to 4 symptoms in the form. <br> 
2. Select your preferred language.  <br>
3. Click <b>Analyze Symptoms</b>.  <br>
4. Scroll down to see diagnosis and description.
</div>
""", unsafe_allow_html=True)

st.markdown("### Note")
st.info("This is a guidance system only. Please consult a doctor for medical advice.")
