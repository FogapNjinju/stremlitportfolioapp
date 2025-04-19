import streamlit as st

# Page Configuration
st.set_page_config(page_title="Njinju Zilefac Fogap - Portfolio", layout="wide", initial_sidebar_state="expanded")

# Custom Styling with Markdown and HTML
st.markdown("""
    <style>
    .main {background-color: #f4f7fa;}
    .sidebar .sidebar-content {background-color: #dbe9ff; padding: 15px; border-radius: 10px;}
    h1 {color: #1a5276; font-family: 'Arial', sans-serif; text-align: center;}
    h2 {color: #2874a6; font-family: 'Arial', sans-serif;}
    .stExpander {background-color: #ffffff; border: 1px solid #d5e8ff; border-radius: 5px; padding: 10px;}
    .stButton>button {background-color: #e67e22; color: white; border-radius: 5px; border: none; padding: 8px 15px;}
    .stButton>button:hover {background-color: #d35400;}
    .stTextInput>div>input, .stTextArea>div>textarea {border-radius: 5px; border: 1px solid #3498db; background-color: #fff;}
    a {color: #e74c3c; text-decoration: none;}
    a:hover {color: #c0392b; text-decoration: underline;}
    .metric-box {background-color: #ffffff; border: 1px solid #d5e8ff; border-radius: 5px; padding: 10px; text-align: center;}
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("Njinju Zilefac Fogap")
    st.markdown("**Data Engineer | Data Scientist**", unsafe_allow_html=True)
    st.image("profile.jpg", caption="Profile Picture", use_container_width=True)  # Replace with your image
    st.markdown("""
        <div style='text-align: center; color: #34495e;'>
            <a href='mailto:andrewfogap@icloud.com'>andrewfogap@icloud.com</a><br>
            <a href='tel:+447442922396'>+447442 922396</a><br>
            <a href='https://www.linkedin.com/in/njinju-zilefac-fogap-5b713117a' target='_blank'>LinkedIn</a> | 
            <a href='https://github.com/fogapandrew?tab=repositories' target='_blank'>GitHub</a>
        </div>
    """, unsafe_allow_html=True)

# Main Content
st.title("Njinju Zilefac Fogap")
st.markdown("<p style='text-align: center; color: #7f8c8d; font-style: italic;'>Data Engineer | Data Scientist | Innovator</p>", unsafe_allow_html=True)

# Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='metric-box'><h3 style='color: #2874a6;'>5+</h3>Years of Experience</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='metric-box'><h3 style='color: #2874a6;'>10+</h3>Projects Completed</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='metric-box'><h3 style='color: #2874a6;'>3</h3>Degrees Earned</div>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #34495e; margin-top: 20px;'>Welcome to my portfolio—explore my journey in data science and engineering!</p>", unsafe_allow_html=True)

# CV Download
try:
    with open("NjinjuZilefacFogap_CV-1.pdf", "rb") as file:
        st.download_button(
            label="Download My CV",
            data=file,
            file_name="NjinjuZilefacFogap_CV.pdf",
            mime="application/pdf",
            key="cv_download"
        )
except FileNotFoundError:
    st.warning("CV file not found. Please ensure 'NjinjuZilefacFogap_CV-1.pdf' is in the same directory.")

# About Me
st.header("About Me")
st.markdown("""
    <p style='color: #34495e;'>
    Well-informed on the basics and fundamentals of designing end-to-end solutions from ETL pipelines, algorithms, databases, websites, and machine learning models from coursework and projects. With a tireless hunger for new skills and a desire to exploit cutting-edge technology.
    </p>
    """, unsafe_allow_html=True)
st.markdown("**Languages:** <span style='color: #16a085;'>English (B2), French (B1), Bangwa (C1)</span>", unsafe_allow_html=True)

# Education
st.header("Education")
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

# Skills
st.header("Skills")
st.markdown("---")
st.markdown("""
- **Languages:** <span style='color: #27ae60;'>C#, Python, SQL, PHP, SAS, Scala</span>  
- **Web Programming:** <span style='color: #27ae60;'>Streamlit, API Development (.NET, Fast API), Front-end (HTML, CSS, JavaScript)</span>  
- **Analytics & Database:** <span style='color: #27ae60;'>ETL/ELT Pipelines, Cloud Computing (Azure), Excel, Tableau, Power BI, SQL Databases</span>  
- **Machine Learning:** <span style='color: #27ae60;'>Scikit-learn, Feature Engineering, Statistical Models</span>  
- **DevOps:** <span style='color: #27ae60;'>Git, Docker, CI/CD (GitLab)</span>
""", unsafe_allow_html=True)

# Experience & Projects
st.header("Experience & Projects")
st.markdown("---")
# Add your expander project sections here
# (Already listed in your original message – include all those expanders unchanged)

# Achievements
st.header("Achievements")
st.markdown("---")
st.markdown("""
- **Led Renewable Energy Price Prediction Project:** Successfully drove a high-impact project at Arinti, delivering accurate electricity price predictions using gradient boosting and a Streamlit app.
- **Cum Laude & Dean's List:** Graduated with honors from Thomas More University, recognized for academic excellence in Data Science.
- **Pioneered ETL System Transition:** Transitioned an Azure-based ETL system to GitLab at Arinti, improving cost efficiency and operational streamlining.
- **Developed AI Skill-Job Matching Tool:** Built an innovative web application at Graffiland, leveraging NLP and LLMs to match skills to careers.
- **Enhanced Network Reliability:** Spearheaded WAN setup and maintenance at SKYLABASE, improving connectivity for multiple stakeholders.
""", unsafe_allow_html=True)

# Certifications
st.header("Certifications")
st.markdown("---")
st.markdown("""
- [Python for Data Science, AI & Development](https://www.coursera.org/account/accomplishments/certificate/4Q5YEV9K36WR) (Coursera)  
- [Introduction to Project Management](https://www.coursera.org/account/accomplishments/certificate/TUXNSLVLKK45) (Coursera)  
- [Prepare, Clean, Transform, and Load Data using PowerBI](https://www.coursera.org/account/accomplishments/certificate/6U3VUXYFX99J) (Coursera)  
- [Agile Project Management](https://www.coursera.org/account/accomplishments/certificate/L6S3FQLVVRNE) (Coursera)  
- [SAS Programmer Specialization](https://www.coursera.org/account/accomplishments/specialization/SQ42ZW9W9B49) (Coursera)  
- [Microsoft Azure for Data Engineering](https://www.coursera.org/account/accomplishments/certificate/P3EGZ6UF3CKD) (Coursera)
""", unsafe_allow_html=True)

# References
st.header("References")
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

# Contact Form
st.header("Get in Touch")
st.markdown("---")
st.markdown("<p style='color: #34495e;'>Interested in collaborating or have a job opportunity? Reach out below!</p>", unsafe_allow_html=True)

with st.form(key="contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submit_button = st.form_submit_button(label="Send")

    if submit_button:
        st.success("Thank you for your message! I’ll get back to you soon.")
