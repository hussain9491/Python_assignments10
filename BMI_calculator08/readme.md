This code and simple bmi calculator is created by me in 4 to 5 mints !

import streamlit as st
st.title("BMI Calculator")

height = st.number_input("Enter your height (in meters):", min_value=0.0, max)
weight = st.number_input("Enter your weight (in kilograms):", min_value=0.0)
final = height ** 2

if st.button("calculate")
    bmi = height / weight
    st.write("Your BMI is: ", bmi)

if bmi < 14.5
st.warning("You are under weight")
elif bmi < 18.5     
st.write("You are normal weight")
else
st.warning("You are over weight")



