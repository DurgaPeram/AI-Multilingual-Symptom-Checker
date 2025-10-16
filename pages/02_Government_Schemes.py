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

st.markdown(
    """
    <style>
    .main .block-container {
        max-width: 1200px;
        width: 95vw;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("### Available Health Schemes")
st.markdown("""
<div class='card'>
<h3><a href="https://abdm.gov.in/">Ayushman Bharat</a></h3>
            <p>The Ayushman Bharat Yojana provides free health coverage of up to ₹5 lakh per family per year. This scheme aims to help economically vulnerable Indians who need healthcare facilities. 
                you can get more information by clicking on the heading.<br>you can register to ABHA by the following link <a href="https://abha.abdm.gov.in/abha/v3/register">Register here</a>
                and for refernce you can go through <a href="https://www.youtube.com/watch?v=dw6qSD8AaxQ">Reference</a>
            </p>
</div>
<div class='card'>
<h3><a href="https://pmjay.gov.in/">Pradhan Mantri Jan Arogya Yojana (PMJAY)</a></h3>
            <p>PMJAY offers cashless and paperless access to services for the beneficiary at the point of service. This is available at both public and empanelled private hospitals in India.
                download the app <a href="https://play.google.com/store/apps/details?id=com.beneficiaryapp&pcampaignid=web_share">Download</a>
                watch these vedios for refernce for <br>
                How to download and log in to the Ayushman Application. Step by Step Guidelines <a href="https://www.youtube.com/watch?v=o6xKT9ph3RI"> Reference 1</a>
                How to do E-KYC and Download the Ayushman Card<a href="https://www.youtube.com/watch?v=F1Jyp1i7VX0">Reference 2</a>
            </p>
</div>
<div class='card'>
            <h3><a href="https://nhm.gov.in/">National Health Mission (NHM)</a></h3>
            <p>The NHM aims to provide accessible, affordable, and quality health care to rural populations, with a focus on reducing infant and maternal mortality rates.</p>
</div>
<div class='card'>
            <h3><a href="https://mohfw.gov.in/">Ministry of Health & Family Welfare</a></h3>
            <p>he Ministry of Health & Family Welfare (MoHFW) is a government ministry in India focused on health policies, family welfare, and the healthcare system. Its primary objectives include formulating and implementing policies that promote healthcare access, improve public health, and ensure family welfare. </p>
</div>
            <div class='card'>
            <h3><a href="https://cghs.gov.in/CghsGovIn/faces/ViewPage.xhtml">Central Government Health Scheme (CGHS)</a></h3>
            <p>This scheme provides healthcare services to Central Government employees, pensioners, and their dependents. It offers medical facilities through a network of wellness centers and empaneled hospitals. </p>
            </div>
            <div class='card'>
             <h3><a href="https://www.poshantracker.in/">Saksham Anganwadi and Poshan 2.0</a></h3>
            <p>These initiatives aim to improve child nutrition and maternal health by upgrading anganwadi centers, which provide services related to early childhood care and nutrition​. </p>
            </div>
            <div class='card'>
            <h3><a href="https://www.india.gov.in/spotlight/rashtriya-swasthya-bima-yojana">Rashtriya Swasthya Bima Yojana (RSBY)</a></h3>
            <p>The workers in the unorganized sector constitute about 93% of the total work force in the country. The Government has been implementing some social security measures for certain occupational groups but the coverage is miniscule. Majority of the workers are still without any social security coverage. One of the major insecurities for workers in the unorganized sector is the frequent incidences of illness and need for medical care and hospitalization of such workers and their family members. Despite the expansion in the health facilities, illness remains one of the most prevalent causes of human deprivation in India.</p>
            </div>
            <div class='card'> <h3><a href="https://www.jeevandayee.gov.in/">Mahatma Jyotirao Phule Jan Arogya Yojana (MJPJAY)</a></h3>
            <p>This scheme offers insurance coverage through United India Insurance Company Ltd. (UIICL) and assurance through State Health Assurance Society (SHAS).</p>
            </div>
            <div class='card'> 
            <a href="https://patient.info/symptom-checker">1.WebMD</a><br>
        <a href="https://symptoms.webmd.com/">2.Patient Symptom Checker</a><br>
        <a href="https://www.verywellhealth.com/health-a-z-4014770">3.verywellhealth A-Z</a>
            </div>
            """, unsafe_allow_html=True)
