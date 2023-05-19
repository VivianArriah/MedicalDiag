import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import pickle 
from sklearn.preprocessing import StandardScaler
st.title("Medical Diagnostic App")
st.markdown("Does the women have diabetes or not ? ")

# step 1 : Load pickled model 
model = open('rfc.pickle', 'rb')
clf = pickle.load(model)
model.close()

# step 2 : create user input from the front end :
pregs = st.number_input('Pregnancies', 0, 20, step = 1)
glucose = st.slider("Glucose", 40,200,20) #last20 is default
bp = st.slider("BloodPressure",20,140,20)
skin = st.slider("SkinThickness",5,100,5)
insulin = st.slider("Insulin", 14.0,846.0,14.0)
bmi = st.slider("BMI",15.0,70.0,15.0)
dpf = st.slider("DiabetesPedigreeFunction", 0.05, 2.50, 0.05)
age = st.slider("Age",21,90,21)

# step 3 : Converting user input to mdoel input 
data = {
    "Pregnancies":pregs,
    "Glucose":glucose,
    "BloodPressure":bp,
    "SkinThickness":skin,
    "Insulin":insulin,
    "BMI":bmi,
    "DiabetesPedigreeFunction":dpf,
    "Age":age
}

input_data = pd.DataFrame([data])
st.write(input_data)


# step 4 : Get prediction model and print it 
prediction = clf.predict(input_data)[0]
if st.button("Prediction"):
    if prediction==1:
        st.error("The woman has Diabetes")
    if prediction==0:
        st.success("The woman is Healthy")
