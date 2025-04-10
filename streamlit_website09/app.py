import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="My Streamlit Website",
    page_icon="🚀",
    layout="wide"
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Data Analysis", "Visualization", "About"])

# Home Page
if page == "Home":
    st.title("Welcome to My Streamlit Website! 🎉")
    st.write("""
    This is a modern website built with Streamlit. Use the sidebar to navigate between different pages.
    """)
    
    # Add some sample content
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Features")
        st.write("""
        - Interactive data analysis
        - Beautiful visualizations
        - Easy navigation
        - Responsive design
        """)
    
    with col2:
        st.header("Get Started")
        st.write("""
        Select a page from the sidebar to explore different features of this website.
        """)

# Data Analysis Page
elif page == "Data Analysis":
    st.title("Data Analysis 📊")
    
    # Create sample data
    data = pd.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100),
        'category': np.random.choice(['A', 'B', 'C'], 100)
    })
    
    st.write("### Sample Data")
    st.dataframe(data)
    
    # Add some interactive elements
    st.write("### Data Summary")
    st.write(data.describe())

# Visualization Page
elif page == "Visualization":
    st.title("Data Visualization 📈")
    
    # Create sample data
    data = pd.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100),
        'category': np.random.choice(['A', 'B', 'C'], 100)
    })
    
    # Create an interactive plot
    fig = px.scatter(data, x='x', y='y', color='category',
                    title='Interactive Scatter Plot')
    st.plotly_chart(fig, use_container_width=True)

# About Page
elif page == "About":
    st.title("About This Website ℹ️")
    st.write("""
    This website was created using Streamlit, a powerful Python library for building web applications.
    
    ### Technologies Used:
    - Streamlit
    - Pandas
    - NumPy
    - Plotly
    
    ### Features:
    - Multi-page navigation
    - Interactive data analysis
    - Beautiful visualizations
    - Responsive design
    """) 