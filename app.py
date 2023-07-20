import streamlit as st
from pathlib import Path
from PIL import Image
import io

current_dir= Path(__file__).parent if "__file_" in locals() else Path.cwd()
css_file= current_dir/ "main.css"

# General settings

EMAIL= "anhad2000bs@gmail.com"
PAGE_TITLE= "Digital CV | Anhad Singh Bhatia"
NAME= "Anhad Singh Bhatia"
SOCIAL_MEDIA= {
    "YouTube":"https://youtube.com/@singhbeyondlimits",
    "LinkedIn": "https://www.linkedin.com/in/anhad-singh-bhatia/",
    "GitHub": "https://github.com/anhadcode",
    "Instagram": "https://www.instagram.com/singh_beyond_limits/" 
}

PROJECTS=[
    "🏆 IPL Win Predictor Probability Project",
    "🏆 DASHBOARD of Netflix and Myntra sales using Tableau and Power BI",
    "🏆 AD- SALES Revenue using Linear Regression"
]

st.set_page_config(page_title=PAGE_TITLE,page_icon=":Wave:")

#LOAD CSS FILE, PDF AND PROFILE PIC

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open("DataAnalystResume.pdf", "rb") as pdf_file:
    PDFbyte= pdf_file.read()

profile_pic= Image.open("profile-pic.png")



# MAIN SECTION
st.header(NAME)
col1, col2= st.columns([1.5,3.5])


with col1:
    profile_pic= Image.open("profile-pic.png")
    
    st.image(profile_pic, use_column_width=True, output_format='JPEG')

with col2:
    #st.title(NAME)
    st.write("""**_Get me data, I will get you good decision_**"")
    st.write("Anhad is an aspiring Data Scientist, who is passionate about Machine Learning and has a decent knowledge of programming and Mathematics.")
    st.download_button(
        label="Download Resume 📄",
        data=PDFbyte,
        file_name="DataAnalystResume.pdf",

    )
    st.write("📧",EMAIL)



###SOCIAL MEDIA###
cols = st.columns(len(SOCIAL_MEDIA))

for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

###EXPERIENCE

st.write("#")
st.subheader("Education Qualification")
st.write(
    """
#### BSc Physics (Hons): University of Delhi
- Scientific Computation with Python
- Mathematical Physics
- Algorithm building 
#### Certication Data Analytics: YMCA Delhi
- Statistics, and Microsoft Access
#### Certification Data Analytics: SSCBS University of Delhi
- Advanced Statistics for Data Analytics, Business Intelligence and Machine Learning
    """
)

st.subheader("Tools and Skills")
columns = st.columns(4)
element= ['Python',"R", "Power BI", "Tableau", "Excel", "Streamlit",
           "Machine Learning", "Statistics","Business Analytics",
           "SQL","SPSS", "KNIME"]
for i, element in enumerate(element):
    column_idx = i % 4  # Alternate between 0 and 1 for the two columns
    columns[column_idx].write(f"""
    - {element}
    """)

st.subheader("Projects and work")
st.write(f"""
- **[Movie Recommender System](https://movierecommender-1xzibkj1icfh.streamlit.app/)** using *[Python: Scikit-Learn, Pandas and Numpy | Algorithm: **Content Based Filtering**]*
- **Netflix Dashboard** using *[Tableau]*
- **Myntra Dashboard** using *[Power BI]*
- **Handwritten Digits Recognition** using *[Python: Scikit-Learn, pandas, and numpy]*
- **[IPL Win prediction](https://ipl-win-predictor-7c8i.onrender.com/)** using *[Python: Scikit-Learn, Pandas and Numpy | Algorithm: **Logistic Regression**]*
- **Salary Prediction** using *[Python: Scikit-Learn, and Pandas | Algorithm: **KNN classification**]*
- **[Flight Prediction](https://flightticketprediction-pxp4bf53l7.streamlit.app/)** using *[Python: Scikit-Learn, Pandas and Numpy | Algorithm: **Random Forest Regression**]*
- **[Employee Promotion Predictor](https://employee-promotion.streamlit.app/)** using *[Python: Scikit-Learn, Pandas and Numpy | Algorithm: **Logistic Regression**]*

""")
st.subheader("Experience")
st.write("""
#### Capline Services [Aug 2022- Jan 2023]
- Managing 4 Offices in California and Texas (United States)
- Claims Management, Denial Management, and Accounts Receivables
- Customer database managment
- Maintaining Customers Dashboard
""")
