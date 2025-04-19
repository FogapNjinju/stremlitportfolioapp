import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit.runtime.media_file_storage import MediaFileStorageError

# Page Configuration
st.set_page_config(page_title="Njinju Zilefac Fogap - Portfolio", layout="wide", initial_sidebar_state="expanded")

# Sidebar
with st.sidebar:
    st.title("Njinju Zilefac Fogap")
    st.markdown("**Data Engineer | Data Scientist**", unsafe_allow_html=True)
    st.image("profile.jpg", caption="Profile Picture", use_container_width=True)  # Replace with your image
    st.markdown("""
        <div style='text-align: center; color: #34495e;'>
            <a href='mailto:andrewfogap@icloud.com'>andrewfogap@icloud.com</a><br>
            <a href='tel:+447442922396'>+447442 922396</a><br>
            <a href='https://www.linkedin.com/in/njinju-zilefac-fogap-5b713117a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app' target='_blank'>LinkedIn</a> | 
            <a href='https://github.com/fogapandrew?tab=repositories' target='_blank'>GitHub</a>
        </div>
    """, unsafe_allow_html=True)
    
    # Theme Toggle
    theme = st.selectbox("Select Theme", ["Light", "Dark"])
    if theme == "Light":
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
            .status-completed {background-color: #2ecc71; color: white; padding: 5px 10px; border-radius: 12px; font-size: 12px; font-weight: bold; display: inline-block; margin-left: 10px;}
            .status-in-progress {background-color: #f39c12; color: white; padding: 5px 10px; border-radius: 12px; font-size: 12px; font-weight: bold; display: inline-block; margin-left: 10px;}
            .quote-box {background-color: #f1f8ff; border-left: 4px solid #3498db; padding: 10px; margin: 10px 0; font-style: italic;}
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            .main {background-color: #2c3e50;}
            .sidebar .sidebar-content {background-color: #34495e; padding: 15px; border-radius: 10px;}
            h1 {color: #ecf0f1; font-family: 'Arial', sans-serif; text-align: center;}
            h2 {color: #bdc3c7; font-family: 'Arial', sans-serif;}
            .stExpander {background-color: #34495e; border: 1px solid #7f8c8d; border-radius: 5px; padding: 10px;}
            .stButton>button {background-color: #e67e22; color: white; border-radius: 5px; border: none; padding: 8px 15px;}
            .stButton>button:hover {background-color: #d35400;}
            .stTextInput>div>input, .stTextArea>div>textarea {border-radius: 5px; border: 1px solid #3498db; background-color: #ecf0f1;}
            a {color: #e74c3c; text-decoration: none;}
            a:hover {color: #c0392b; text-decoration: underline;}
            .metric-box {background-color: #34495e; border: 1px solid #7f8c8d; border-radius: 5px; padding: 10px; text-align: center;}
            .status-completed {background-color: #2ecc71; color: white; padding: 5px 10px; border-radius: 12px; font-size: 12px; font-weight: bold; display: inline-block; margin-left: 10px;}
            .status-in-progress {background-color: #f39c12; color: white; padding: 5px 10px; border-radius: 12px; font-size: 12px; font-weight: bold; display: inline-block; margin-left: 10px;}
            .quote-box {background-color: #2c3e50; border-left: 4px solid #3498db; padding: 10px; margin: 10px 0; font-style: italic; color: #ecf0f1;}
            </style>
        """, unsafe_allow_html=True)

# Main Content
st.title("Njinju Zilefac Fogap")
st.markdown("<p style='text-align: center; color: #7f8c8d; font-style: italic;'>Data Engineer | Data Scientist | Innovator</p>", unsafe_allow_html=True)

# Metrics Section
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='metric-box'><h3 style='color: #2874a6;'>5+</h3>Years of Experience</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='metric-box'><h3 style='color: #2874a6;'>10+</h3>Projects Completed</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='metric-box'><h3 style='color: #2874a6;'>3</h3>Degrees Earned</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #34495e; margin-top: 20px;'>Welcome to my portfolio—explore my journey in data science and engineering!</p>", unsafe_allow_html=True)

# CV Download Button (Placeholder)
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

# Education Section
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

# Skills Section
st.header("Skills")
st.markdown("---")
st.markdown("""
- **Languages:** <span style='color: #27ae60;'>C#, Python, SQL, PHP, SAS, Scala</span>
- **Web Programming:** <span style='color: #27ae60;'>Streamlit, API Development (.NET, Fast API), Front-end (HTML, CSS, JavaScript)</span>
- **Analytics & Database:** <span style='color: #27ae60;'>ETL/ELT Pipelines, Cloud Computing (Azure), Excel, Tableau, Power BI, SQL Databases</span>
- **Machine Learning:** <span style='color: #27ae60;'>Scikit-learn, Feature Engineering, Statistical Models</span>
- **DevOps:** <span style='color: #27ae60;'>Git, Docker, CI/CD (GitLab)</span>
""", unsafe_allow_html=True)

# Experience & Projects Section
st.header("Experience & Projects")
st.markdown("---")
with st.expander("Data Engineer - Data Scientist Intern @ Arinti"):
    col1, col2 = st.columns([1, 4])
    with col1:
        try:
            st.image("arinti_thumbnail.jpg", width=100)
        except (FileNotFoundError, MediaFileStorageError):
            st.write("Thumbnail not found")
    with col2:
        st.markdown("**Project:** Renewable Energy Price Prediction in Belgium <span class='status-completed'>Completed</span>", unsafe_allow_html=True)
        st.write("""
        - Led the project, driving the prediction of electricity prices.
        - Conducted a comprehensive three-phase exploratory analysis to uncover trends in the energy market across different periods: pre, during, and post-COVID.
        - Pioneered the development of an ETL system utilizing Azure Datalakes, Databricks and Datafactories and Datawarehouse, later transitioning to GitLab for enhanced cost efficiency. Instituted a robust CI/CD pipeline to streamline operations.
        - Implemented machine learning algorithms, employing three models, and ultimately selecting gradient boosting for its superior accuracy in price prediction.
        - Successfully deployed the machine learning model via a user-friendly Streamlit web application, enhancing accessibility and usability for stakeholders.
        - Developed a Power BI dashboard to provide insightful visualizations, aiding in the interpretation of data and facilitating informed decision-making.
        """)
        # Interactive Visualization
        data = pd.DataFrame({
            "Period": ["Pre-COVID", "During-COVID", "Post-COVID"],
            "Avg Price (€/MWh)": [50, 70, 60]
        })
        fig = px.bar(data, x="Period", y="Avg Price (€/MWh)", title="Electricity Price Trends")
        st.plotly_chart(fig, use_container_width=True)
    st.markdown("[View Project](https://github.com/fogapandrew?tab=repositories)", unsafe_allow_html=True)
with st.expander("AI Skill-Job Machine Web Application @ Graffiland, Tienen, Belgium"):
    col1, col2 = st.columns([1, 4])
    with col1:
        try:
            st.image("graffiland_thumbnail.jpg", width=100)
        except (FileNotFoundError, MediaFileStorageError):
            st.write("Thumbnail not found")
    with col2:
        st.markdown("**Aug 2023 - Dec 2023** <span class='status-completed'>Completed</span>", unsafe_allow_html=True)
        st.write("""
        - Contributed to the development of an AI Skill-Job Machine Web Application, guiding clients to suitable careers based on CVs and survey responses.
        - Collaborated with a team of three to design and implement an ETL (Extract, Transform, Load) processing system for cleaning and structuring clients' curriculum vitae and survey data. Utilized GitHub for version control and seamless collaboration.
        - Employed Natural Language Processing (NLP) techniques and regular expressions (regex) to mask personal information in the client data, ensuring privacy and confidentiality.
        - Implemented Langchain, utilizing large language models (LLMs) such as ChatGPT, for prompt engineering, enhancing the quality and relevance of the model's output.
        - Utilized Flask frameworks for web application development, incorporating HTML and CSS for user interface design. Leveraged Azure Functions and GitHub Actions for efficient deployment and continuous integration.
        - Implemented MLFlow for model tracking, enabling efficient monitoring and management of machine learning models throughout the development lifecycle.
        - Utilized Prefect for orchestrating and managing the workflow, ensuring smooth execution of tasks and processes within the project.
        """)
    st.markdown("[View Project](https://github.com/fogapandrew?tab=repositories)", unsafe_allow_html=True)
with st.expander("University Projects @ Thomas More, Mechelen, Belgium"):
    col1, col2 = st.columns([1, 4])
    with col1:
        try:
            st.image("thomasmore_thumbnail.jpg", width=100)
        except (FileNotFoundError, MediaFileStorageError):
            st.write("Thumbnail not found")
    with col2:
        st.markdown("**Jan 2021 - Jan 2024** <span class='status-completed'>Completed</span>", unsafe_allow_html=True)
        st.write("""
        - Conducted comprehensive data analysis, managed missing values without leakage, engineered features, employed cross-validated feature selection, and optimized model parameters to develop a Random Forest regression model, enhancing mean house price prediction.
        - Implemented a Prophet-based time series forecasting model for Auckland's daily cycling counts, enhancing accuracy by incorporating Waitangi Day 2018 as a holiday, evaluated performance via RMSE calculation, visualized forecasted values to elucidate holiday impact, and continuously improved the model through proactive problem-solving.
        - Developed an AI solution in C# to predict weight contributed by specific ingredients, utilizing KNN and multi linear regression models, with no external libraries, and conducting comprehensive model comparison to optimize accuracy and performance.
        - Collaborated with other developers on a school project to create a Birthday calendar web application.
        - Currently working part time at Swirlwavez on an AI home automation project <span class='status-in-progress'>In Progress</span>.
        """)
    st.markdown("[View Projects](https://github.com/fogapandrew?tab=repositories)", unsafe_allow_html=True)
with st.expander("University Projects @ Wolverhampton, United Kingdom"):
    col1, col2 = st.columns([1, 4])
    with col1:
        try:
            st.image("wolverhampton_thumbnail.jpg", width=100)
        except (FileNotFoundError, MediaFileStorageError):
            st.write("Thumbnail not found")
    with col2:
        st.markdown("**Nov 2024 - Jan 2026** <span class='status-in-progress'>In Progress</span>", unsafe_allow_html=True)
        st.write("""
        - This project performs an exploratory data analysis of the "Survival from Malignant Melanoma" dataset (1962-1977, Denmark) using R, examining 205 patients' survival time, tumor thickness, age, sex, and ulceration through statistics, visualizations, correlations, and hypothesis testing, revealing outliers and gender differences.
        - Analyzed and visualized 124K+ Dutch traffic accident records using SAS Visual Analytics to identify trends, offender profiles, and safety gaps; built multi-dashboard insights and forecasts for public policy optimization.
        - TransSync is a university-developed Transport Management System that digitizes travel agency operations in Cameroon with features like agency and client management, online booking, secure payments, analytics, and a robust Oracle-based database designed with 3NF normalization, security, and concurrency control.
        - DataMiningInformaticsHub: A comprehensive project portfolio from the University of Wolverhampton's Data Mining and Informatics course (7CS033), demonstrating expertise in data preprocessing, classification, clustering, association rule mining, and sentiment analysis using Python on diverse real-world datasets, including "adult", online retail transactions, and Twitter data.
        """)
        # Interactive Visualization
        data = pd.DataFrame({
            "Year": [2018, 2019, 2020, 2021],
            "Accidents": [15000, 14500, 13000, 14000]
        })
        fig = px.line(data, x="Year", y="Accidents", title="Dutch Traffic Accidents Trend")
        st.plotly_chart(fig, use_container_width=True)
    st.markdown("[View Projects](https://github.com/FogapNjinju?tab=repositories)", unsafe_allow_html=True)
with st.expander("Data Engineering Projects, United Kingdom"):
    col1, col2 = st.columns([1, 4])
    with col1:
        try:
            st.image("bookharvest_thumbnail.jpg", width=100)
        except (FileNotFoundError, MediaFileStorageError):
            st.write("Thumbnail not found")
    with col2:
        st.markdown("**Jan 2025 - Present** <span class='status-in-progress'>In Progress</span>", unsafe_allow_html=True)
        st.write("""
        - BookHarvest: A Python data pipeline that extracts book details (titles, authors, ratings, covers) from APIs, web pages, and CSVs, stores them in SQLite, and serves them via a Flask API, using requests, BeautifulSoup, pandas, and sqlite3.
        """)
    st.markdown("[View Projects](https://github.com/FogapNjinju/BookHarvest/tree/main)", unsafe_allow_html=True
