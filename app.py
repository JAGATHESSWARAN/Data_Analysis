from operator import index
import streamlit as st
import plotly.express as px
from pycaret.regression import setup, compare_models, pull, save_model, load_model
import pandas_profiling
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import os 

if os.path.exists('./dataset.csv'): 
    df = pd.read_csv('dataset.csv', index_col=None)

# # Set page config with the logo
# st.set_page_config(page_title="Build0Brain", page_icon="https://drive.google.com/file/d/1LKzO7-5rNZndwbpMmavGM7K9E-IfKUcu/view?usp=sharing")

# # Add logo to the top right corner
# st.image("https://drive.google.com/file/d/1LKz", width=100)

with st.sidebar:
    st.title("AutoGenML")
    video_file = open("Logo.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes, autoplay=True)
    choice = st.radio("Navigation", ["Vision","About Us"])   
    st.info("of this applications")
st.title("🔍JAGZ Data Master📈")
if choice == "Vision":
    st.header("Our Vision at Build0Brain")
    st.write("""
    💫At Build0Brain, we envision a future where data-driven decision making is accessible to everyone, 
    regardless of their technical background. Our AutoNickML project is a testament to this vision, 
    aiming to democratize data science and machine learning.""")
    st.image("https://i.ibb.co/RpybsM2/Designer.png", width=300)
    st.write("""
    💫We believe in empowering individuals and organizations with the tools to unlock the potential 
    hidden within their data. By automating complex analytical processes, we're bridging the gap 
    between raw data and actionable insights, enabling our users to make informed decisions quickly 
    and confidently.

    💫Our goal is to cultivate a data-literate society where the power of analytics is at everyone's 
    fingertips, fostering innovation and driving progress across all sectors.""")
    st.balloons()
    

if choice == "About Us":
    st.title("About Build0Brain")
    st.write("""
    🎗️Build0Brain is a pioneering tech company at the forefront of automated data analysis and 
    machine learning solutions. Founded by a team of passionate data scientists and software 
    engineers, we set out on a mission to make advanced analytics accessible to all.

    🎗️Our flagship project, AutoNickML, is the culmination of years of research and development 
    in the field of automated machine learning. It represents our commitment to simplifying 
    complex data processes and empowering users to derive meaningful insights without extensive 
    technical knowledge.""")
    #st.image("")
    st.write("""
    At Build0Brain, we're driven by a set of core values:
    1. Innovation: We constantly push the boundaries of what's possible in data science.
    2. Accessibility: We believe in democratizing access to advanced analytical tools.
    3. Integrity: We uphold the highest standards of data ethics and responsible AI.
    4. User-Centric Design: We prioritize user experience in all our solutions.

    🎗️Our team comprises diverse talents from various backgrounds, united by a common goal: 
    to revolutionize how the world interacts with data. We're not just building tools; 
    we're building a future where data-driven decision making is the norm, not the exception.

    Join us on this exciting journey as we continue to innovate and shape the future of 
    data analysis and machine learning.
    """)

        
#     st.title("Upload Your Dataset")
#     file = st.file_uploader("Upload Your Dataset")
#     if file: 
#         df = pd.read_csv(file, index_col=None)
#         df.to_csv('dataset.csv', index=None)
#         st.dataframe(df)

# if choice == "Profiling": 
#     st.title("Exploratory Data Analysis")
#     profile_df = df.profile_report()
#     st_profile_report(profile_df)

# if choice == "Modelling": 
#     chosen_target = st.selectbox('Choose the Target Column', df.columns)
#     if st.button('Run Modelling'): 
#         setup(df, target=chosen_target, silent=True)
#         setup_df = pull()
#         st.dataframe(setup_df)
#         best_model = compare_models()
#         compare_df = pull()
#         st.dataframe(compare_df)
#         save_model(best_model, 'best_model')

# if choice == "Download": 
#     with open('best_model.pkl', 'rb') as f: 
#         st.download_button('Download Model', f, file_name="best_model.pkl")
    
