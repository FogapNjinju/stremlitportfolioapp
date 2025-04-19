import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Njinju Zilefac Fogap - Portfolio",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

# Title and subtitle
st.title("Njinju Zilefac Fogap")
st.markdown("**Data Engineer | Data Scientist**")

# Contact Information
st.sidebar.header("Contact")
st.sidebar.write("📧 andrewfogap@icloud.com")
st.sidebar.write("📞 +447442 922396")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/njinju-zilefac-fogap-5b713117a)")
st.sidebar.markdown("[GitHub](https://github.com/fogapandrew?tab=repositories)")

# Download CV
with open("NjinjuZilefacFogap_CV-1.pdf", "rb") as file:
    st.download_button("Download My CV", file, "NjinjuZilefacFogap_CV.pdf", mime="application/pdf")

# About Me
st.header("About Me")
st.write("""
Well-informed on the basics and fundamentals of designing end-to-end solutions from ETL pipelines, algorithms, databases, websites, and machine learning models from coursework and projects. 
With a tireless hunger for new skills and a desire to exploit cutting-edge technology.
""")

# Education
st.header("Education")
st.write("**MSc Data Science** - University of Wolverhampton, UK (Nov 2024 - Present)")
st.write("Concentrations: Computing and Mathematics")
st.write("**B.S. Information Management and Multimedia** - Thomas More University of Applied Science")
st.write("Concentrations: Business and Data Science, GPA: Cum Laude, Dean's List")
st.write("**B.S. Computer Engineering (Telecommunication)** - University of Buea")
st.write("Concentrations: Computer Systems and Telecommunication, GPA: 3.0/4, Good")

# Skills
st.header("Skills")
st.write("""
- **Languages:** C#, Python, SQL, PHP, SAS, Scala  
- **Web Programming:** Streamlit, API Development (.NET, Fast API), Front-end (HTML, CSS, JavaScript)  
- **Analytics & Database:** ETL/ELT Pipelines, Cloud Computing (Azure), Excel, Tableau, Power BI, SQL Databases  
- **Machine Learning:** Scikit-learn, Feature Engineering, Statistical Models  
- **DevOps:** Git, Docker, CI/CD (GitLab)
""")

# Experience & Projects
st.header("Experience & Projects")

with st.expander("💡 Renewable Electricity Price Prediction App (Arinti)"):
    st.write("""
    - Developed an application to predict renewable electricity prices using gradient boosting models.
    - Leveraged pandas, scikit-learn, and Streamlit to build an interactive dashboard for analysis and visualization.
    """)

with st.expander("📦 Azure Data Engineering Pipelines & Monitoring (Arinti)"):
    st.write("""
    - Maintained and extended ETL/ELT pipelines in Azure Data Factory for automated ingestion and transformation.
    - Transitioned pipelines from Azure to GitLab CI/CD for efficiency and cost reduction.
    """)

with st.expander("🧠 AI Career Matching App using Streamlit & NLP (Graffiland)"):
    st.write("""
    - Built a web app using Streamlit that matches user skills to ideal career paths using OpenAI embeddings and LLMs.
    - Collected job roles from Belgian sites, stored in PostgreSQL, and developed semantic search engine using NLP.
    """)

with st.expander("📊 Heart Disease Risk Prediction (University of Wolverhampton)"):
    st.write("""
    - Trained multiple machine learning models on UCI Heart dataset to predict heart disease risks.
    - Evaluated and visualized performance using ROC curves, accuracy, and validation curves.
    """)

with st.expander("🏨 Hospital Pharmacy Stock Management App (Thomas More)"):
    st.write("""
    - Designed a stock and price tracking dashboard for hospital pharmacies using Streamlit and Plotly.
    - Implemented classification models to predict drug shortages and optimize purchasing.
    """)

with st.expander("📱 Web App Development for Travel Agency (Personal Project)"):
    st.write("""
    - Built a full-stack web app for travel agency management in Cameroon.
    - Replaced paper-based ticketing with online booking and payment system using Flask and MongoDB.
    """)

with st.expander("🌐 Network Design & Telecom Cabling (SKYLABASE)"):
    st.write("""
    - Designed WAN and wireless communication solutions for clients in Cameroon.
    - Installed and maintained CAT 5/6 cabling, network switches, modems, and routers.
    """)

# Achievements
st.header("Achievements")
st.write("""
- 🎯 Led a project at Arinti to predict renewable electricity prices using ML and Streamlit.
- 🏅 Graduated Cum Laude and was on the Dean's List at Thomas More University.
- 🔁 Transitioned an ETL system from Azure Data Factory to GitLab CI/CD, improving efficiency.
- 🤖 Built an AI-based career matching tool using LLMs and OpenAI at Graffiland.
- 🧰 Developed a stock monitoring dashboard for hospitals to combat drug shortages.
- 🌍 Designed and implemented network connectivity solutions across regions in Cameroon.
""")

# Certifications
st.header("Certifications")
st.write("""
- [Python for Data Science, AI & Development](https://www.coursera.org/account/accomplishments/certificate/4Q5YEV9K36WR)
- [Introduction to Project Management](https://www.coursera.org/account/accomplishments/certificate/TUXNSLVLKK45)
- [Prepare, Clean, Transform, and Load Data using PowerBI](https://www.coursera.org/account/accomplishments/certificate/6U3VUXYFX99J)
- [Agile Project Management](https://www.coursera.org/account/accomplishments/certificate/L6S3FQLVVRNE)
- [SAS Programmer Specialization](https://www.coursera.org/account/accomplishments/specialization/SQ42ZW9W9B49)
- [Microsoft Azure for Data Engineering](https://www.coursera.org/account/accomplishments/certificate/P3EGZ6UF3CKD)
""")

# References
st.header("References")
st.write("""
- **Mr. Fernando Lovera** – Data Engineer at Arinti  
  📧 fernando.loveratorres@thomasmore.be  
  📞 Available upon request

- **Mr. Collin Van der Vorst** – Course Coordinator at Thomas More University  
  📧 collin.vandervorst@thomasmore.be  
  📞 Available upon request
""")

# Contact Form
st.header("Get in Touch")
with st.form(key="contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submit_button = st.form_submit_button(label="Send")

    if submit_button:
        st.success("Thank you for your message! I’ll get back to you soon.")
