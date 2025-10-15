import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components
import base64
import os
from utils_AI import ai_diagnose

# ✅ Streamlit Page Config
st.set_page_config(page_title=" AI Symptom Checker (Multilingual)", layout="wide")

BASE_DIR = Path(__file__).parent
STATIC = BASE_DIR / "static"
STYLES = BASE_DIR / "styles"

# ✅ Load Custom CSS
if (STYLES / "base.css").exists():
    st.markdown(f"<style>{(STYLES/'base.css').read_text()}</style>", unsafe_allow_html=True)

# ✅ Background & Header
st.markdown("""
    <style>
    body {
        background: url('https://static.vecteezy.com/system/resources/thumbnails/042/585/516/small_2x/ai-generated-medical-stethoscope-on-green-background-top-view-with-copy-space-photo.jpg')
        no-repeat center center fixed;
        background-size: cover;
    }
    .blur-bg {
        backdrop-filter: blur(8px);
        background: rgba(255,255,255,0.3);
        min-height: 100vh;
        width: 100vw;
        position: fixed;
        top: 0;
        left: 0;
        z-index: -1;
    }
    </style>
    <div class="blur-bg"></div>
""", unsafe_allow_html=True)

# ✅ Header Section
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.image(str(STATIC / "images/icon.png"), width=110)
with col2:
    st.markdown("<h1 style='color:#1565c0;text-align:center;'> Welcome to Multiligual Symptom Checker</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:#333;'>Analyze your symptoms using AI and get health insights in your preferred language.</p>", unsafe_allow_html=True)
with col3:
    st.image(str(STATIC / "images/medical.jpg"), width=110)

# ✅ Slideshow + Symptom Input Layout
left, right = st.columns([2, 2])

with left:
    st.markdown("### 👩🏻‍⚕️ Prevention is better than Cure")
    image_files = ["image 0.jpg", "image 1.jpg", "image 2.jpg", "image 3.jpg", "image 4.jpg", "image 6.jpg"]
    img_tags = ""
    for i, img_name in enumerate(image_files):
        img_path = STATIC / "images" / img_name
        if img_path.exists():
            with open(img_path, "rb") as f:
                data = f.read()
            b64 = base64.b64encode(data).decode()
            img_tags += f'<img src="data:image/jpeg;base64,{b64}" class="slide{" active" if i == 0 else ""}">\n'
    components.html(f"""
    <style>
    .slideshow-container {{ position: relative; width: 100%; max-width: 450px; height: 350px; margin: auto; overflow: hidden; border-radius: 10px; }}
    .slide {{ display: none; width: 100%; height: 350px; object-fit: cover; border-radius: 10px; }}
    .slide.active {{ display: block; }}
    </style>
    <div class="slideshow-container">{img_tags}</div>
    <script>
    var slides=document.querySelectorAll('.slide');var i=0;
    setInterval(()=>{{slides.forEach(s=>s.classList.remove('active'));slides[i].classList.add('active');i=(i+1)%slides.length;}},2500);
    </script>
    """, height=360)

with right:
    st.markdown("### 🤒 Enter Your Symptoms")
    if "symptom_inputs" not in st.session_state:
        st.session_state.symptom_inputs = [""]

    for i in range(len(st.session_state.symptom_inputs)):
        st.session_state.symptom_inputs[i] = st.text_input(f"Symptom {i+1}", st.session_state.symptom_inputs[i], key=f"symptom_{i}")

    if len(st.session_state.symptom_inputs) < 4:
        if st.button("➕ Add Symptom"):
            st.session_state.symptom_inputs.append("")
    else:
        st.warning("⚠️ Maximum 4 symptoms allowed.")

    # 🌍 Language Selection
    language_map = {
        "English 🇬🇧": "en",
        "Telugu 🇮🇳": "te",
        "Hindi 🇮🇳": "hi",
        "Tamil 🇮🇳": "ta",
        "Kannada 🇮🇳": "kn",
        "Malayalam 🇮🇳": "ml",
        "Bengali 🇮🇳": "bn",
        "Gujarati 🇮🇳": "gu",
        "Marathi 🇮🇳": "mr",
        "Urdu 🇮🇳": "ur",
        "French 🇫🇷": "fr",
        "Spanish 🇪🇸": "es"
    }
    selected_lang = st.selectbox("📜 Select Output Language", list(language_map.keys()))
    selected_lang_code = language_map[selected_lang]

    analyze_clicked = st.button("🔍 Analyze Symptoms")

# ✅ AI Diagnosis
if analyze_clicked:
    symptoms = [s.strip() for s in st.session_state.symptom_inputs if s.strip()]
    if symptoms:
        with st.spinner("🧠 AI analyzing your symptoms..."):
            ai_result = ai_diagnose(symptoms, lang=selected_lang_code)

        if "error" in ai_result:
            st.error(ai_result["error"])
        else:
            disease = ai_result.get("disease", "Unknown Disease")
            desc = ai_result.get("description_en", "")
            causes = ai_result.get("causes", "")
            precautions = ai_result.get("precautions", "")
            when_help = ai_result.get("when_to_seek_help", "")
            confidence = ai_result.get("confidence", 0.0)

            st.markdown(f"""
            <div style="background:#f5f9ff;padding:25px;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,0.1);margin-top:25px;">
                <h2 style="color:#1565c0;">🩺 {disease}</h2>
                <p>{desc}</p>
                <h4>🧬 Causes</h4><p>{causes}</p>
                <h4>🩹 Precautions</h4><p>{precautions}</p>
                <h4>🏥 When to Seek Help</h4><p>{when_help}</p>
                <p style="color:#777;">🤖 Confidence: {confidence:.2f}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter at least one symptom before analyzing.")
