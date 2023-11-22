# to view the web app in the browser ,run the command as : streamlit run <filename.py> in the terminal 
import streamlit as st
from PIL import Image
from streamlit import *

st.set_page_config(page_title = "BMI Calculator by Sai Kumar",page_icon = ":tada:",layout = "wide")

st.title("BMI Calculator")
st.write("-------------------------------------------------")

img = Image.open("imagebmi.jpg")
st.image(img)

st.text_input("Name :"," ")
st.radio(label = "Gender : ",options=('Male','Female'))

st.number_input("Age :",value = False)

st.text_area("Address :")

st.write("Hobbies :")
st.checkbox("Watching Movies")
st.checkbox("Listening Music")
st.checkbox("Playing Games")
st.checkbox("Singing Songs")
st.checkbox("Coding Consistency")
st.checkbox("Exploring World")

weight = st.number_input("Enter Your Weight(Kg) :",step = 1,value = False)

height = st.number_input("Enter Your Height(Cm) :",step = 1,value = True)

BMI = weight/(height)**2

BMI = BMI * 10000

st.success(f"Your BMI Value is {BMI} kg/m^2")

if BMI >= 18.5 and BMI <= 24.9:
    st.success(f"You are Healthy :heart_eyes:")
else:
    st.warning(f"You are UnHealthy :disappointed_relieved:")
     
#Footer 
    
    with st.container():
        st.write("--------")
        left_column,right_column = st.columns(2);
        
        with left_column:
            st.header("About Me -")
            st.write('''
        I am Sai Kumar Tonupunuri,
        Third Year B-Tech Student pursuing Computer Science Of Engineering 
        in Bharath Institute Of Higher Education And Research,Chennai.
                     ''')
            
        with right_column:
            st.header("Connect with Me -")
            st.write("[E-Mail](saikumartonupunuri@gmail.com)")
            st.write("[LinkedIn](https://www.linkedin.com/in/sai-kumar-tonupunuri)")
            st.write("[GitHub](https://github.com/saikumar-tonupunuri)")
        
        
st.write('--------')
st.write('----- © 2023,Sai Kumar -----')