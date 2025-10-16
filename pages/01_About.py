import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
STYLES = BASE_DIR / "styles"
STATIC = BASE_DIR / "static"
st.markdown(f"<style>{(STYLES/'base.css').read_text()}</style>", unsafe_allow_html=True)
# Header
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.image(str(STATIC / "images/icon.png"), width=130)
with col2:
    st.markdown("<h1 style='color:#1565c0;text-align:center;'> Welcome to Multiligual Symptom Checker</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:#333;'>Analyze your symptoms using AI and get health insights in your preferred language.</p>", unsafe_allow_html=True)
with col3:
    st.image(str(STATIC / "images/medical.jpg"), width=130)


# Content
st.markdown("## Our Mission")
st.markdown("<div class='card' style='border-left:5px solid green;'>Provide accessible healthcare guidance worldwide.</div>", unsafe_allow_html=True)

st.markdown("## How It Works")
st.markdown("<div class='card' style='border-left:5px solid purple;'>Enter symptoms → system analyzes → suggests possible diagnoses in your chosen language.</div>", unsafe_allow_html=True)

st.markdown("## Why Choose Us?")
st.markdown("""
<div class='card' style='border-left:5px solid orange;'>
<ul>
<li>🌍 Multilingual Support</li>
<li>📚 Comprehensive Database</li>
<li>💻 User-friendly interface</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("## Meet the Team")
st.markdown("<div class='card' style='border-left:5px solid teal;'>Developers, healthcare professionals, and linguists collaborating together.</div>", unsafe_allow_html=True)
