import numpy as np
import pickle 
import streamlit as st  

scaler=pickle.load(open("scaler_standard.pkl", "rb"))
model = pickle.load(open("prediction.pkl", "rb"))

    
    # Give a title
st.title('Diabetes Prediction Web App')
    
    # To get the input data from the user
Pregnancies = st.number_input('Number of Pregnancies')
Glucose = st.number_input('Glucose Level')
BloodPressure = st.number_input('Blood Pressure value')
SkinThickness = st.number_input('Skin Thickness value')
Insulin = st.number_input('Insulin Level')
BMI = st.number_input('BMI value')
DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value')
Age = st.number_input('Age of person')
    
new_data=scaler.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
predict=model.predict(new_data)

if st.button("Diabetic Result"):
    if predict[0] ==1 :
        st.success("Diabetes")
       
    else:
        
        st.success(" NON-Diabetic ")

    
    
    
    
    
    
    
    
    
    
    
    
    
