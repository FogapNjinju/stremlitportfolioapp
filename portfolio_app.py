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
    .status-completed {background-color: #2ecc71; color: white; padding: 5px 10px; border-radius: 12px; font-size: 12px; font-weight: bold; display: inline-block; margin-left: 10px;}
    .status-in-progress {background-color: #f39c12; color: white; padding: 5px 10px; border-radius: 12px; font-size: 12px; font-weight: bold; display: inline-block; margin-left: 10px;}
    </style>
""", unsafe_allow_html=True)

# Experience & Projects Section
st.header("Experience & Projects")
st.markdown("---")
with st.expander("Data Engineer - Data Scientist Intern @ Arinti"):
    st.markdown("**Project:** Renewable Energy Price Prediction in Belgium <span class='status-completed'>Completed</span>", unsafe_allow_html=True)
    st.write("""
    - Led the project, driving the prediction of electricity prices.
    - Conducted a comprehensive three-phase exploratory analysis to uncover trends in the energy market across different periods: pre, during, and post-COVID.
    - Pioneered the development of an ETL system utilizing Azure Datalakes, Databricks and Datafactories and Datawarehouse, later transitioning to GitLab for enhanced cost efficiency. Instituted a robust CI/CD pipeline to streamline operations.
    - Implemented machine learning algorithms, employing three models, and ultimately selecting gradient boosting for its superior accuracy in price prediction.
    - Successfully deployed the machine learning model via a user-friendly Streamlit web application, enhancing accessibility and usability for stakeholders.
    - Developed a Power BI dashboard to provide insightful visualizations, aiding in the interpretation of data and facilitating informed decision-making.
    """)
    st.markdown("[View Project](https://github.com/fogapandrew?tab=repositories)", unsafe_allow_html=True)
with st.expander("AI Skill-Job Machine Web Application @ Graffiland, Tienen, Belgium"):
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
    st.markdown("**Nov 2024 - Jan 2026** <span class='status-in-progress'>In Progress</span>", unsafe_allow_html=True)
    st.write("""
    - This project performs an exploratory data analysis of the "Survival from Malignant Melanoma" dataset (1962-1977, Denmark) using R, examining 205 patients' survival time, tumor thickness, age, sex, and ulceration through statistics, visualizations, correlations, and hypothesis testing, revealing outliers and gender differences.
    - Analyzed and visualized 124K+ Dutch traffic accident records using SAS Visual Analytics to identify trends, offender profiles, and safety gaps; built multi-dashboard insights and forecasts for public policy optimization.
    - TransSync is a university-developed Transport Management System that digitizes travel agency operations in Cameroon with features like agency and client management, online booking, secure payments, analytics, and a robust Oracle-based database designed with 3NF normalization, security, and concurrency control.
    - DataMiningInformaticsHub: A comprehensive project portfolio from the University of Wolverhampton's Data Mining and Informatics course (7CS033), demonstrating expertise in data preprocessing, classification, clustering, association rule mining, and sentiment analysis using Python on diverse real-world datasets, including "adult", online retail transactions, and Twitter data.         
    """)
    st.markdown("[View Projects](https://github.com/FogapNjinju?tab=repositories)", unsafe_allow_html=True)
with st.expander("Data Engineering Projects, United Kingdom"):
    st.markdown("**Jan 2025 - Present** <span class='status-in-progress'>In Progress</span>", unsafe_allow_html=True)
    st.write("""
    - BookHarvest: A Python data pipeline that extracts book details (titles, authors, ratings, covers) from APIs, web pages, and CSVs, stores them in SQLite, and serves them via a Flask API, using requests, BeautifulSoup, pandas, and sqlite3.
    """)
    st.markdown("[View Projects](https://github.com/FogapNjinju/BookHarvest/tree/main)", unsafe_allow_html=True)
with st.expander("Traineeship @ Foundation of Applied Statistics and Data Management (FASTDAM), Buea, Cameroon"):
    st.markdown("**Dec 2019 - May 2020** <span class='status-completed'>Completed</span>", unsafe_allow_html=True)
    st.write("""
    - Undertook comprehensive training in basic statistics, mastering tools such as SPSS, Epi Data, and Microsoft Excel.
    - Engaged in hands-on projects involving data preprocessing utilizing Epi Data and Excel, and statistical analysis using SPSS.
    - Developed proficiency in statistical analysis software such as IBM SPSS Statistics and Epi Data.
    - Enhanced my data management skills, particularly in handling and analyzing data using Python programming language and Microsoft Excel.
    """)
    st.markdown("[View Work](https://github.com/fogapandrew?tab=repositories)", unsafe_allow_html=True)
with st.expander("Job @ SKYLABASE, Buea, Cameroon"):
    st.markdown("**April 2016 - June 2018** <span class='status-completed'>Completed</span>", unsafe_allow_html=True)
    st.write("""
    - Collaborated within a team of 6 professionals, taking charge of monitoring and deploying internet services.
    - Demonstrated expertise in Linux and Ubuntu environments, facilitating effective network administration.
    - Managed LAN-WAN configurations, ensuring seamless connectivity and optimal performance.
    - Spearheaded the setup and maintenance of Wide Area Networks (WAN), contributing to improved network accessibility and reliability.
    """)
    st.markdown("[View Work](https://github.com/fogapandrew?tab=repositories)", unsafe_allow_html=True)
