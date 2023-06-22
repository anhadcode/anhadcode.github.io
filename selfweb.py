import streamlit as st
import webbrowser
from PIL import Image

#####################################
col1,col2= st.columns(2)
with col1:
    st.header("Anhad Singh Bhatia")
    st.write("Data Scientist, Statistician, and Musician")
    "### Education"
    "BSc Physics (Hons)- University of Delhi"
    "Certification- Data Analytics and Business Intelligence- University of Delhi"

with col2:
    img= Image.open('photo.JPG')
    img= img.resize((230,300))
    st.image(img)
###################################################################

c1, c2,c3,c4= st.columns(4)
with c1:
    if st.button("LinkedIn"):
        webbrowser.open_new_tab("https://www.linkedin.com/in/anhad-singh-bhatia/")

with c2:
    if st.button("Github"):
        webbrowser.open_new_tab("https://github.com/anhadcode")

with c3:
    if st.button("Youtube"):
        webbrowser.open_new_tab("https://www.youtube.com/channel/UCXqDUvEgYP2Bpqdi5tU2Fgg")

with c4:
    if st.button("Instagram"):
        webbrowser.open_new_tab("https://www.instagram.com/singh_beyond_limits/")

"### Skills"
element= ['Data Analytics', "Data Mining","Data Visualisation", "Data cleaning", "Machine Learning",
         "Statistics","Web apps","Information Theory","NLP","Deep Learning"]



columns = st.columns(5)

# Iterate through the elements and display them in the columns
for i, element in enumerate(element):
    column_idx = i % 5  # Alternate between 0 and 1 for the two columns
    columns[column_idx].write(element)

"### Tools"
tools= ['Python','Power BI',"Tableau","Jupyter Notebook", "Sklearn","Streamlit","SQL","Excel"
        ,"Pyspark","SPSS","R programming"]
#######################################################################
#LOADING PHOTOS OF THE TOOLS

logo= ['excel.png','jupyter.png', 'powerbi.png', 'py.png', 'pyspark.png', 'r.png' ,'sklearn.png', 
       'spss.png', 'sql.png', 'str.png', 'tab.png', "pandas.png", "matplot.png", "seaborn.png"]
columns1= st.columns(6)*3


def print_logo(i):
    with columns1[i]:
        
        st.image(logo[i])

for i in range(len(logo)):
    print_logo(i)

############################################

"### Experience"
"**Capline Services- Associate [Aug 2022-Jan 2023]**"
st.markdown("""
- Database management of the pateients
- Claims managments
- Account Receivables
- Denial Management
- Client Interactions
""")




