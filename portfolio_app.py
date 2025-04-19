import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit.runtime.media_file_storage import MediaFileStorageError

# Page Configuration
st.set_page_config(page_title="Njinju Zilefac Fogap - Portfolio", layout="wide", initial_sidebar_state="expanded")

# Theme Persistence
if "theme" not in st.session_state:
    st.session_state.theme = "Light"

# Sidebar
with st.sidebar:
    st.title("Njinju Zilefac Fogap")
    st.markdown("**Data Engineer | Data Scientist**", unsafe_allow_html=True)
    try:
        st.image("profile.jpg", caption="Profile Picture", use_container_width=True, alt="Njinju Zilefac Fogap's profile picture")
    except (FileNotFoundError, MediaFileStorageError):
        st.image("https://via.placeholder.com/150", caption="Profile Picture", use_container_width=True, alt="Placeholder profile picture")
    st.markdown("""
        <div style='text-align: center; color: #34495e;'>
            <a href='mailto:andrewfogap@icloud.com'>andrewfogap@icloud.com</a><br>
            <a href='tel:+447442922396'>+447442 922396</a><br>
            <a href='https://www.linkedin.com/in/njinju-zilefac-fogap-5b713117a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app' target='_blank'>LinkedIn</a> | 
            <a href='https://github.com/fogapandrew?tab=repositories' target='_blank'>GitHub</a>
        </div>
    """, unsafe_allow_html=True)
    
    # Navigation Menu
    st.markdown("""
    <div style='margin-top: 20px;'>
        <strong>Navigate</strong><br>
        <a href='#about-me'>About Me</a><br>
        <a href='#education'>Education</a><br>
        <a href='#skills'>Skills</a><br>
        <a href='#experience-projects'>Experience & Projects</a><br>
        <a href='#achievements'>Achievements</a><br>
        <a href='#certifications'>Certifications</a><br>
        <a href='#references'>References</a><br>
        <a href='#get-in-touch'>Contact</a>
    </div>
    """, unsafe_allow_html=True)
    
    # Theme Toggle
    theme = st.selectbox("Select Theme", ["Light", "Dark", "High Contrast"], index=["Light", "Dark", "High Contrast"].index(st.session_state.theme))
    st.session_state.theme = theme
    
    # CSS for Themes
    if theme == "Light":
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&family=Poppins&display=swap');
        .main { background-color: #f4f7fa; }
        .sidebar .sidebar-content { background-color: #dbe9ff; padding: 15px; border-radius: 10px; }
        h1 { color: #1a5276; font-family: 'Roboto', sans-serif; font-weight: 700; text-align: center; }
        h2 { color: #2874a6; font-family: 'Roboto', sans-serif; font-weight: 600; }
        p, li, a { font-family: 'Poppins', sans-serif; }
        .stExpander { background-color: #ffffff; border: 1px solid #d5e8ff; border-radius: 5px; padding: 10px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); }
        .stButton>button { background-color: #e67e22; color: white; border-radius: 5px; border: none; padding: 8px 15px; }
        .stButton>button:hover { background-color: #d35400; }
        .stTextInput>div>input, .stTextArea>div>textarea { border-radius: 5px; border: 1px solid #3498db; background-color: #fff; }
        a { color: #e74c3c; text-decoration: none; }
        a:hover { color: #c0392b; text-decoration: underline; }
        .metric-box { background-color: #ffffff; border: 1px solid #d5e8ff; border-radius: 8px; padding: 10px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); }
        .status-completed { background-color: #2ecc71; color: white; padding: 5px 10px; border-radius: 12px; font-size: 12px; font-weight: bold; display: inline-block; margin-left: 10px; }
        .status-in-progress { background-color: #f39c12; color: white; padding: 5px 10px; border-radius: 12px; font-size: 12px; font-weight: bold; display: inline-block; margin-left: 10px; }
        .quote-box { background-color: #f1f8ff; border-left: 4px solid #3498db; padding: 10px; margin: 10px 0; font-style: italic; }
        img[alt="Profile Picture"], img[alt="Placeholder profile picture"] { border-radius: 50%; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
        img { loading: lazy; }
        @media (max-width: 768px) {
            h1 { font-size: 24px; }
            h2 { font-size: 20px; }
            p, li { font-size: 16px; }
            .sidebar img { width: 80px; }
        }
        </style>
        """, unsafe_allow_html=True)
    elif theme == "Dark":
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&family=Poppins&display=swap');
        .main { background-color: #2c3e50; }
        .sidebar .sidebar-content { background-color: #34495e; padding: 15px; border-radius: 10px; }
        h1 { color: #ecf0f1; font-family: 'Roboto', sans-serif; font-weight: 700; text-align: center; }
        h2 { color: #bdc3c7; font-family: 'Roboto', sans-serif; font-weight: 600; }
        p, li, a { font-family: 'Poppins', sans-serif; color: #ecf0f1; }
        .stExpander { background-color: #34495e; border: 1px solid #7f8c8d; border-radius: 5px; padding: 10px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); }
        .stButton>button { background Wrote 6144 chars, showing first 6144:import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit.runtime.media_file_storage import MediaFileStorageError

# Page Configuration
st.set_page_config(page_title="Njinju Zilefac Fogap - Portfolio", layout="wide", initial_sidebar_state="expanded")

# Theme Persistence
if "theme" not in st.session_state:
    st.session_state.theme = "Light"

# Sidebar
with st.sidebar:
    st.title("Njinju Zilefac Fogap")
    st.markdown("**Data Engineer | Data Scientist**", unsafe_allow_html=True)
    try:
        st.image("profile.jpg", caption="Profile Picture", use_container_width=True, alt="Njinju Zilefac Fogap's profile picture")
    except (FileNotFoundError, MediaFileStorageError):
        st.image("https://via.placeholder.com/150", caption="Profile Picture", use_container_width=True, alt="Placeholder profile picture")
    st.markdown("""
        <div style='text-align: center; color: #34495e;'>
            <a href='mailto:andrewfogap@icloud.com'>andrewfogap@icloud.com</a><br>
            <a href='tel:+447442922396'>+447442 922396</a><br>
            <a href='https://www.linkedin.com/in/njinju-zilefac-fogap-5b713117a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app' target='_blank'>LinkedIn</a> | 
            <a href='https://github.com/fogapandrew?tab=repositories' target='_blank'>GitHub</a>
        </div>
    """, unsafe_allow_html=True)
    
    # Navigation Menu
    st.markdown("""
    <div style='margin-top: 20px;'>
        <strong>Navigate</strong><br>
        <a href='#about-me'>About Me</a><br>
        <a href='#education'>Education</a><br>
        <a href='#skills'>Skills</a><br>
        <a href='#experience-projects'>Experience & Projects</a><br>
        <a href='#achievements'>Achievements</a><br>
        <a href='#certifications'>Certifications</a><br>
        <a href='#references'>References</a><br>
        <a href='#get-in-touch'>Contact</a>
    </div>
    """, unsafe_allow_html=True)
    
    # Theme Toggle
    theme = st.selectbox("Select Theme", ["Light", "Dark", "High Contrast"], index=["Light", "Dark", "High Contrast"].index(st.session_state.theme))
    st.session_state.theme = theme
    
    # CSS for Themes
    if theme == "Light":
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&family=Poppins&display=swap');
        .main { background-color: #f4f7fa; }
        .sidebar .sidebar-content { background-color: #dbe9ff; padding: 15px; border-radius: 10px; }
        h1 { color: #1a5276; font-family: 'Roboto', sans-serif; font-weight: 700; text-align: center; }
        h2 { color: #2874a6; font-family: 'Roboto', sans-serif; font-weight: 600; }
        p, li, a { font-family: 'Poppins', sans-serif; }
        .stExpander { background-color: #ffffff; border: 1px solid #d5e8ff; border-radius: 5px; padding: 10px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); }
        .stButton>button { background-color: #e67e22; color: white; border-radius: 5px; border: none; padding: 8px 15px; }
        .stButton>button:hover { background-color: #d35400; }
        .stTextInput>div>input, .stTextArea>div>textarea { border-radius: 5px; border: 1px solid #3498db; background-color: #fff; }
        a { color: #e74c3c; text-decoration: none; }
        a:hover { color: #c0392b; text-decoration: underline; }
        .metric-box { background-color: #ffffff; border: 1px solid #d5e8ff; border-radius: 8px; padding: 10px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); }
        .status-completed { background-color: #2ecc71; color: white; padding: 5px 10px; border-radius: 12px; font-size: 12px; font-weight: bold; display: inline-block; margin-left: 10px; }
        .status-in-progress { background-color: #f39c12; color: white; padding: 5px 10px; border-radius: 12px; font-size: 12px; font-weight: bold; display: inline-block; margin-left: 10px; }
        .quote-box { background-color: #f1f8ff; border-left: 4px solid #3498db; padding: 10px; margin: 10px 0; font-style: italic; }
        img[alt="Profile Picture"], img[alt="Placeholder profile picture"] { border-radius: 50%; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
        img { loading: lazy; }
        @media (max-width: 768px) {
            h1 { font-size: 24px; }
            h2 { font-size: 20px; }
            p, li { font-size: 16px; }
            .sidebar img { width: 80px; }
        }
        </style>
        """, unsafe_allow_html=True)
    elif theme == "Dark":
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&family=Poppins&display=swap');
        .main { background-color: #2c3e50; }
        .sidebar .sidebar-content { background-color: #34495e; padding: 15px; border-radius: 10px; }
        h1 { color: #ecf0f1; font-family: 'Roboto', sans-serif; font-weight: 700; text-align: center; }
        h2 { color: #bdc3c7; font-family: 'Roboto', sans-serif; font-weight: 600; }
        p, li, a { font-family: 'Poppins', sans-serif; color: #ecf0f1; }
        .stExpander { background-color: #34495e; border: 1px solid #7f8c8d; border-radius: 5px; padding: 10px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); }
        .stButton>button { background-color: #e67e22; color: white; border-radius: 5px; border: none; padding: 8px 15px; }
        .stButton>button:hover { background-color: #d35400; }
        .stTextInput>div>input, .stTextArea>div>textarea { border-radius: 5px; border: 1px solid #3498db; background-color: #ecf0f1; }
        a { color: #e74c3c; text-decoration: none; }
        a:hover { color: #c0392b; text-decoration: underline; }
        .metric-box { background-color: #34495e; border: 1px solid #7f8c8d; border-radius: 8px; padding: 10px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); }
        .status-completed { background-color: #2ecc71; color: white; padding: 5px 10px; border-radius: 12px; font-size: 12px; font-weight: bold; display: inline-block; margin-left: 10px; }
        .status-in-progress { background-color: #f39c12; color: white; padding: 5px 10px; border-radius: 12px; font-size: 12px; font-weight: bold; display: inline-block; margin-left: 10px; }
        .quote-box { background-color: #2c3e50; border-left: 4px solid #3498db; padding: 10px; margin: 10px 0; font-style: italic; color: #ecf0f1; }
        img[alt="Profile Picture"], img[alt="Placeholder profile picture"] { border-radius: 50%; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
        img { loading: lazy; }
        @media (max-width: 768px) {
            h1 { font-size: 24px; }
            h2 { font-size: 20px; }
            p, li { font-size: 16px; }
            .sidebar img { width: 80px; }
        }
        </style>
        """, unsafe_allow_html=True)
    else:  # High Contrast
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&family=Poppins&display=swap');
        .main { background-color: #000; color: #fff; }
        .sidebar .sidebar-content { background-color: #333; padding: 15px; border-radius: 10px; }
        h1 { color: #fff; font-family: 'Roboto', sans-serif; font-weight: 700; text-align: center; }
        h2 { color: #fff; font-family: 'Roboto', sans-serif; font-weight: 600; }
        p, li, a { font-family: 'Poppins', sans-serif; color: #fff; }
        .stExpander { background-color: #333; border: 1px solid #fff; border-radius: 5px; padding: 10px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); }
        .stButton>button { background-color: #ff0; color: #000; border-radius: 5px; border: none; padding: 8px 15px; }
        .stButton>button:hover { background-color: #cc0; }
        .stTextInput>div>input, .stTextArea>div>textarea { border-radius: 5px; border: 1px solid #fff; background-color: #333; color: #fff; }
        a { color: #ff0; text-decoration: none; }
        a:hover { color: #cc0; text-decoration: underline; }
        .metric-box { background-color: #333; border: 1px solid #fff; border-radius: 8px; padding: 10px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); }
        .status-completed { background-color: #0f0; color: #000; padding: 5px 10px; border-radius: 12px; font-size: 12px; font-weight: bold; display: inline-block; margin-left: 10px; }
        .status-in-progress { background-color: #ff0; color: #000; padding: 5px 10px; border-radius: 12px; font-size: 12px; font-weight: bold; display: inline-block; margin-left: 10px; }
        .quote-box { background-color: #333; border-left: 4px solid #fff; padding: 10px; margin: 10px 0; font-style: italic; color: #fff; }
        img[alt="Profile Picture"], img[alt="Placeholder profile picture"] { border-radius: 50%; box-shadow: 0 4px 8px rgba(255, 255, 255, 0.2); }
        img { loading: lazy; }
        @media (max-width: 768px) {
            h1 { font-size: 24px; }
            h2 { font-size: 20px; }
            p, li { font-size: 16px; }
            .sidebar img { width: 80px; }
        }
        </style>
        """, unsafe_allow_html=True)

# Main Content
st.markdown("<h1 id='main'>Njinju Zilefac Fogap</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: #7f8c8d; font-style: italic;'>Data Engineer | Data Scientist | Innovator</p>",
    unsafe_allow_html=True
)

# Metrics Section
if st.get_option("theme.base") == "mobile":
    cols = st.columns(1)
    with cols[0]:
        st.markdown("<div class='metric-box'><h3 style='color: #2874a6;'>5+</h3>Years of Experience</div>", unsafe_allow_html=True)
        st.markdown("<div class='metric-box'><h3 style='color: #2874a6;'>10+</h3>Projects Completed</div>", unsafe_allow_html=True)
        st.markdown("<div class='metric-box'><h3 style='color: #2874a6;'>3</h3>Degrees Earned</div>", unsafe_allow_html=True)
else:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='metric-box'><h3 style='color: #2874a6;'>5+</h3>Years of Experience</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='metric-box'><h3 style='color: #2874a6;'>10+</h3>Projects Completed</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='metric-box'><h3 style='color: #2874a6;'>3</h3>Degrees Earned</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #34495e; margin-top: 20px;'>Welcome to my portfolio—explore my journey in data science and engineering!</p>", unsafe_allow_html=True)

# CV Download and Preview
st.subheader("My Resume")
try:
    with open("NjinjuZilefacFogap_CV-1.pdf", "rb") as file:
        st.download_button(
            label="📄 Download My CV",
            data=file,
            file_name="NjinjuZilefacFogap_CV.pdf",
            mime="application/pdf",
            key="cv_download"
        )
    st.markdown("""
    <iframe src='NjinjuZilefacFogap_CV-1.pdf' width='100%' height='600px' style='border: none;'></iframe>
    """, unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("CV file not found | Please ensure 'NjinjuZilefacFogap_CV-1.pdf' is in the same directory.")

# About Me
st.markdown("<h1 id='about-me'>About Me</h1>", unsafe_allow_html=True)
st.markdown("""
    <p style='color: #34495e;'>
    Well-informed on the basics and fundamentals of designing end-to-end solutions from ETL pipelines, algorithms, databases, websites, and machine learning models from coursework and projects. With a tireless hunger for new skills and a desire to exploit cutting-edge technology.
    </p>
    """, unsafe_allow_html=True)
st.markdown("**Languages:** <span style='color: #16a085;'>English (B2), French (B1), Bangwa (C1)</span>", unsafe_allow_html=True)

# Education Section
st.markdown("<h1 id='education'>Education</h1>", unsafe_allow_html=True)
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.subheader("MSc Data Science")
    st.markdown("*University of Wolverhampton, UK*", unsafe_allow_html=True)
    st.write("Nov 2024 - Present")
    st.markdown("<span style='color: #8e44ad;'>Concentrations: Computing and Mathematics</span>", unsafe_allow_html=True)
with col2:
    st.subheader("B.S. Information Management and Multimedia")
    st.markdown("*Thomas More University of Applied Science*", unsafe_allow_html=True)
    st.write("Concentrations: Business and Data Science")
    st.write("GPA: Cum Laude, Dean's List")
st.subheader("B.S. Computer Engineering (Telecommunication)")
st.markdown("*University of Buea*", unsafe_allow_html=True)
st.write("Concentrations: Computer Systems and Telecommunication")
st.write("GPA: 3.0/4, Good")

# Skills Section
st.markdown("<h1 id='skills'>Skills</h1>", unsafe_allow_html=True)
st.markdown("---")
@st.cache_data
def load_skills_data():
    return pd.DataFrame({
        "Skill": ["Python", "SQL", "C#", "Streamlit", "Azure", "Tableau", "Scikit-learn", "Docker"],
        "Proficiency": [90, 85, 80, 75, 70, 65, 70, 60]
    })
skills = load_skills_data()
fig = px.bar(skills, x="Skill", y="Proficiency", title="Skill Proficiency", color="Skill")
fig.update_traces(hovertemplate="Skill: %{x}<br>Proficiency: %{y}%")
st.plotly_chart(fig, use_container_width=True)
st.markdown("""
- **Languages:** <span style='color: #27ae60;'>C#, Python, SQL, PHP, SAS, Scala</span>
- **Web Programming:** <span style='color: #27ae60;'>Streamlit, API Development (.NET, Fast API), Front-end (HTML, CSS, JavaScript)</span>
- **Analytics & Database:** <span style='color: #27ae60;'>ETL/ELT Pipelines, Cloud Computing (Azure), Excel, Tableau, Power BI, SQL Databases</span>
- **Machine Learning:** <span style='color: #27ae60;'>Scikit-learn, Feature Engineering, Statistical Models</span>
- **DevOps:** <span style='color: #27ae60;'>Git, Docker, CI/CD (GitLab)</span>
""", unsafe_allow_html=True)

# Experience & Projects Section
st.markdown("<h1 id='experience-projects'>Experience & Projects</h1>", unsafe_allow_html=True)
st.markdown("---")
project_filter = st.multiselect("Filter Projects", ["All", "Completed", "In Progress"], default="All")
if "All" in project_filter or "Completed" in project_filter:
    with st.expander("Data Engineer - Data Scientist Intern @ Arinti"):
        col1, col2 = st.columns([1, 4])
        with col1:
            try:
                st.image("arinti_thumbnail.jpg", width=100, alt="Arinti project thumbnail")
            except (FileNotFoundError, MediaFileStorageError):
                st.image("https://via.placeholder.com/100", width=100, alt="Placeholder thumbnail")
        with col2:
            st.markdown("**Project:** Renewable Energy Price Prediction in Belgium <span class='status-completed'>Completed</span>", unsafe_allow_html=True)
            st.write("""
            - Built ETL pipeline with Azure and GitLab, reducing costs by 20%.
            - Deployed gradient boosting model via Streamlit, improving accuracy by 15%.
            - Developed Power BI dashboard for stakeholder insights.
            """)
            @st.cache_data
            def load_energy_data():
                return pd.DataFrame({
                    "Period": ["Pre-COVID", "During-COVID", "Post-COVID"],
                    "Avg Price (€/MWh)": [50, 70, 60]
                })
            data = load_energy_data()
            fig = px.bar(data, x="Period", y="Avg Price (€/MWh)", title="Electricity Price Trends")
            fig.update_traces(hovertemplate="Period: %{x}<br>Price: €%{y}")
            st.plotly_chart(fig, use_container_width=True)
        st.markdown("[View Project](https://github.com/fogapandrew?tab=repositories)", unsafe_allow_html=True)
    with st.expander("AI Skill-Job Machine Web Application @ Graffiland, Tienen, Belgium"):
        col1, col2 = st.columns([1, 4])
        with col1:
            try:
                st.image("graffiland_thumbnail.jpg", width=100, alt="Graffiland project thumbnail")
            except (FileNotFoundError, MediaFileStorageError):
                st.image("https://via.placeholder.com/100", width=100, alt="Placeholder thumbnail")
        with col2:
            st.markdown("**Aug 2023 - Dec 2023** <span class='status-completed'>Completed</span>", unsafe_allow_html=True)
            st.write("""
            - Developed AI web app matching skills to careers using NLP and LLMs.
            - Implemented ETL system with Flask and Azure Functions for data processing.
            - Used MLFlow and Prefect for model tracking and workflow orchestration.
            """)
        st.markdown("[View Project](https://github.com/fogapandrew?tab=repositories)", unsafe_allow_html=True)
    with st.expander("University Projects @ Thomas More, Mechelen, Belgium"):
        col1, col2 = st.columns([1, 4])
        with col1:
            try:
                st.image("thomasmore_thumbnail.jpg", width=100, alt="Thomas More project thumbnail")
            except (FileNotFoundError, MediaFileStorageError):
                st.image("https://via.placeholder.com/100", width=100, alt="Placeholder thumbnail")
        with col2:
            st.markdown("**Jan 2021 - Jan 2024** <span class='status-completed'>Completed</span>", unsafe_allow_html=True)
            st.write("""
            - Built Random Forest model for house price prediction, improving accuracy by 10%.
            - Developed Prophet-based forecasting for cycling counts, reducing RMSE by 12%.
            - Created C# AI solution for ingredient weight prediction using KNN.
            """)
        st.markdown("[View Projects](https://github.com/fogapandrew?tab=repositories)", unsafe_allow_html=True)
if "All" in project_filter or "In Progress" in project_filter:
    with st.expander("University Projects @ Wolverhampton, United Kingdom"):
        col1, col2 = st.columns([1, 4])
        with col1:
            try:
                st.image("wolverhampton_thumbnail.jpg", width=100, alt="Wolverhampton project thumbnail")
            except (FileNotFoundError, MediaFileStorageError):
                st.image("https://via.placeholder.com/100", width=100, alt="Placeholder thumbnail")
        with col2:
            st.markdown("**Nov 2024 - Jan 2026** <span class='status-in-progress'>In Progress</span>", unsafe_allow_html=True)
            st.write("""
            - Analyzed melanoma dataset with R, identifying key survival factors.
            - Visualized Dutch traffic accidents with SAS, optimizing public policy.
            - Developed TransSync TMS with Oracle database for travel agencies.
            """)
            @st.cache_data
            def load_accident_data():
                return pd.DataFrame({
                    "Year": [2018, 2019, 2020, 2021],
                    "Accidents": [15000, 14500, 13000, 14000]
                })
            data = load_accident_data()
            fig = px.line(data, x="Year", y="Accidents", title="Dutch Traffic Accidents Trend")
            fig.update_traces(hovertemplate="Year: %{x}<br>Accidents: %{y}")
            st.plotly_chart(fig, use_container_width=True)
        st.markdown("[View Projects](https://github.com/FogapNjinju?tab=repositories)", unsafe_allow_html=True)
    with st.expander("Data Engineering Projects, United Kingdom"):
        col1, col2 = st.columns([1, 4])
        with col1:
            try:
                st.image("bookharvest_thumbnail.jpg", width=100, alt="BookHarvest project thumbnail")
            except (FileNotFoundError, MediaFileStorageError):
                st.image("https://via.placeholder.com/100", width=100, alt="Placeholder thumbnail")
        with col2:
            st.markdown("**Jan 2025 - Present** <span class='status-in-progress'>In Progress</span>", unsafe_allow_html=True)
            st.write("""
            - Built BookHarvest pipeline with Python, extracting book data via APIs.
            - Stored data in SQLite and served via Flask API.
            """)
        st.markdown("[View Projects](https://github.com/FogapNjinju/BookHarvest/tree/main)", unsafe_allow_html=True)
if "All" in project_filter or "Completed" in project_filter:
        with st.expander("Traineeship @ Foundation of Applied Statistics and Data Management (FASTDAM), Buea, Cameroon"):
            col1, col2 = st.columns([1, 4])
            with col1:
                try:
                    st.image("fastdam_thumbnail.jpg", width=100, alt="FASTDAM project thumbnail")
                except (FileNotFoundError, MediaFileStorageError):
                    st.image("https://via.placeholder.com/100", width=100, alt="Placeholder thumbnail")
            with col2:
                st.markdown("**Dec 2019 - May 2020** <span class='status-completed'>Completed</span>", unsafe_allow_html=True)
                st.write("""
                - Mastered SPSS, Epi Data, and Excel for statistical analysis.
                - Conducted data preprocessing and analysis with Python.
                """)
            st.markdown("[View Work](https://github.com/fogapandrew?tab=repositories)", unsafe_allow_html=True)
        with st.expander("Job @ SKYLABASE, Buea, Cameroon"):
            col1, col2 = st.columns([1, 4])
            with col1:
                try:
                    st.image("skylabase_thumbnail.jpg", width=100, alt="SKYLABASE project thumbnail")
                except (FileNotFoundError, MediaFileStorageError):
                    st.image("https://via.placeholder.com/100", width=100, alt="Placeholder thumbnail")
            with col2:
                st.markdown("**April 2016 - June 2018** <span class='status-completed'>Completed</span>", unsafe_allow_html=True)
                st.write("""
                - Managed LAN-WAN configurations for optimal performance.
                - Set up Wide Area Networks, improving connectivity by 25%.
                """)
            st.markdown("[View Work](https://github.com/fogapandrew?tab=repositories)", unsafe_allow_html=True)

# Achievements Section
st.markdown("<h1 id='achievements'>Achievements</h1>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
- **Led Renewable Energy Price Prediction:** Delivered accurate predictions, reducing costs by 20% at Arinti.
- **Cum Laude & Dean's List:** Graduated with honors from Thomas More University.
- **Pioneered ETL Transition:** Migrated Azure ETL to GitLab, saving 15% in operational costs.
- **Developed AI Skill-Job Tool:** Built NLP-based career matching app at Graffiland.
- **Enhanced Network Reliability:** Improved WAN connectivity by 25% at SKYLABASE.
""", unsafe_allow_html=True)

# Certifications Section
st.markdown("<h1 id='certifications'>Certifications</h1>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
- [Python for Data Science, AI & Development](https://www.coursera.org/account/accomplishments/certificate/4Q5YEV9K36WR) (Coursera)
- [Introduction to Project Management](https://www.coursera.org/account/accomplishments/certificate/TUXNSLVLKK45) (Coursera)
- [Prepare, Clean, Transform, and Load Data using PowerBI](https://www.coursera.org/account/accomplishments/certificate/6U3VUXYFX99J) (Coursera)
- [Agile Project Management](https://www.coursera.org/account/accomplishments/certificate/L6S3FQLVVRNE) (Coursera)
- [SAS Programmer Specialization](https://www.coursera.org/account/accomplishments/specialization/SQ42ZW9W9B49) (Coursera)
- [Microsoft Azure for Data Engineering](https://www.coursera.org/account/accomplishments/certificate/P3EGZ6UF3CKD) (Coursera)
""", unsafe_allow_html=True)

# References Section
st.markdown("<h1 id='references'>References</h1>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
- **Mr. Fernando Lovera**
  *Data Engineer, Arinti*
  Email: fernando.loveratorres@thomasmore.be
  Phone: Available upon request
- **Mr. Collin Van der Vorst**
  *Course Coordinator, Thomas More University*
  Email: collin.vandervorst@thomasmore.be
  Phone: Available upon request
""", unsafe_allow_html=True)
st.write("Contact details provided upon request to respect privacy.")

# Testimonials Subsection
st.subheader("Testimonials")
st.markdown("""
<div class='quote-box'>
"Njinju's ability to lead complex data projects with precision and innovation is truly remarkable. His work on the energy price prediction project was outstanding."
— <strong>Mr. Fernando Lovera</strong>, Data Engineer, Arinti
</div>
<div class='quote-box'>
"Njinju is a dedicated and talented individual with a strong grasp of data science concepts. His contributions to our academic projects were invaluable."
— <strong>Mr. Collin Van der Vorst</strong>, Course Coordinator, Thomas More University
</div>
""", unsafe_allow_html=True)

# Contact Form
st.markdown("<h1 id='get-in-touch'>Get in Touch</h1>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<p style='color: #34495e;'>Interested in collaborating or have a job opportunity? Reach out below!</p>", unsafe_allow_html=True)
with st.form(key="contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit_button = st.form_submit_button(label="Send Message")
    if submit_button:
        # Uncomment and configure for Formspree integration
        # import requests
        # response = requests.post(
        #     "https://formspree.io/f/your_form_id",
        #     data={"name": name, "email": email, "message": message}
        # )
        # if response.status_code == 200:
        #     st.success(f"Thank you, {name}! Your message has been sent.")
        # else:
        #     st.error("Failed to send message. Please try again.")
        st.success(f"Thank you, {name}! I'll respond to your message at {email} soon.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #7f8c8d;'>© 2025 Njinju Zilefac Fogap | Built with Streamlit</p>", unsafe_allow_html=True)
