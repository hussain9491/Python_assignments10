# Simple BMI Calculator Assignment 08

import streamlit as st
import numpy as np

# Page config
st.set_page_config(
    page_title="Professional BMI Calculator",
    page_icon="⚖️",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("⚖️ Professional BMI Calculator")
st.markdown("""
    Calculate your Body Mass Index (BMI) to assess your weight status. 
    BMI is a simple way to check if your weight is in a healthy range.
    """)

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input(
        "Enter Your Weight (kg)",
        min_value=20.0,
        max_value=300.0,
        value=70.0,
        step=0.1,
        help="Enter your weight in kilograms"
    )

with col2:
    height = st.number_input(
        "Enter Your Height (cm)",
        min_value=100.0,
        max_value=250.0,
        value=170.0,
        step=0.1,
        help="Enter your height in centimeters"
    )

# BMI Categories
bmi_categories = {
    "Underweight": {"min": 0, "max": 18.5, "color": "#3498db"},
    "Normal": {"min": 18.5, "max": 24.9, "color": "#2ecc71"},
    "Overweight": {"min": 25.0, "max": 29.9, "color": "#f1c40f"},
    "Obese": {"min": 30.0, "max": 100, "color": "#e74c3c"}
}

if st.button("Calculate BMI", type="primary"):
    # Convert height from cm to meters
    height_m = height / 100
    # Calculate BMI
    bmi = weight / (height_m ** 2)
    bmi_rounded = round(bmi, 1)
    
    # Determine category
    category = next(
        (cat for cat, range_ in bmi_categories.items() 
         if range_["min"] <= bmi < range_["max"]),
        "Obese"
    )
    
    # Display results in a card
    st.markdown(f"""
    <div class="metric-card">
        <h2 style="text-align: center;">Your Results</h2>
        <h1 style="text-align: center; color: {bmi_categories[category]['color']};">{bmi_rounded}</h1>
        <p style="text-align: center; font-size: 1.2em;">{category}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Progress bar
    progress = (bmi - bmi_categories["Underweight"]["min"]) / (
        bmi_categories["Obese"]["max"] - bmi_categories["Underweight"]["min"]
    )
    st.progress(min(1.0, max(0.0, progress)))
    
    # Health information
    st.markdown("### Health Information")
    if category == "Underweight":
        st.info("""
        - Consider consulting a nutritionist
        - Focus on nutrient-dense foods
        - Consider strength training to build muscle
        """)
    elif category == "Normal":
        st.success("""
        - Maintain your current healthy lifestyle
        - Continue regular physical activity
        - Eat a balanced diet
        """)
    elif category == "Overweight":
        st.warning("""
        - Consider increasing physical activity
        - Focus on portion control
        - Choose whole, unprocessed foods
        """)
    else:
        st.error("""
        - Consult with a healthcare provider
        - Consider a structured weight loss program
        - Focus on sustainable lifestyle changes
        """)
    
    # Additional metrics
    st.markdown("### Additional Information")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Healthy BMI Range", "18.5 - 24.9")
    with col2:
        st.metric("Your Category", category)

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: gray;">
        <p>Note: BMI is a screening tool and not a diagnostic measure of body fat or health.</p>
        <p>Consult with healthcare professionals for personalized advice.</p>
    </div>
    """, unsafe_allow_html=True)