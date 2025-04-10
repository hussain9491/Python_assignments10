1. Importing Libraries
python
Copy
Edit
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st:
Yeh line Streamlit library ko import karti hai aur use "st" alias ke saath refer karti hai. Streamlit se web apps banana bahut aasan ho jata hai.
("Yeh code Streamlit library ko import karta hai jisse web applications develop kiye ja sakte hain.")

import pandas as pd:
Pandas library ko import karta hai jisse hum structured data (jaise DataFrame) ke saath kam kar sakte hain.
("Pandas ko import kiya gaya hai jo data manipulation aur analysis ke liye bahut mufeed hai.")

import numpy as np:
NumPy library ko import karta hai jo numerical computations aur array operations ke liye use hoti hai.
("NumPy array aur mathematical operations ke liye use hoti hai, isko 'np' alias se refer kiya jata hai.")

import plotly.express as px:
Plotly Express ko import karta hai jo interactive visualizations (charts, graphs) banane ke liye use hota hai.
("Plotly Express visualization create karne ke liye ek powerful tool hai, isko 'px' ke naam se import kiya gaya hai.")

2. Page Configuration
python
Copy
Edit
st.set_page_config(
    page_title="My Streamlit Website",
    page_icon="🚀",
    layout="wide"
)
st.set_page_config(...):
Is function ka istemaal app ke page ke configuration set karne ke liye hota hai.

page_title="My Streamlit Website":
Yeh title browser tab me nazar aayega.

page_icon="🚀":
Yeh icon tab ke sath nazar aayega.

layout="wide":
Is se page horizontally pure screen ka use karta hai, wide layout activate hota hai.
("Yeh configuration settings se aapki website ka title, icon aur layout set hota hai.")

3. Sidebar Navigation
python
Copy
Edit
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Data Analysis", "Visualization", "About"])
st.sidebar.title("Navigation"):
Sidebar pe ek title display karta hai jise "Navigation" kehte hain.
("Sidebar me title add kar raha hai jo navigation ke liye user ko guide karta hai.")

page = st.sidebar.radio("Go to", ["Home", "Data Analysis", "Visualization", "About"]):
Yeh ek radio button create karta hai jisme chaar options diye gaye hain: Home, Data Analysis, Visualization aur About.

Jo option select hota hai, uska value variable page me store ho jata hai.
("Radio button se user ko alag alag pages select karne ka option milta hai.")

4. Home Page Code
python
Copy
Edit
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
if page == "Home":
Agar selected page "Home" hai, to yeh block execute hoga.

st.title("Welcome to My Streamlit Website! 🎉"):
Page pe bada title display karta hai jo user ka khushamdeed kehta hai.
("Yeh welcome message display karta hai jab user home page pe aata hai.")

st.write(""" ... """):
Yeh multi-line string ko display karta hai, jisme website ke bare me brief information di gai hai.
("Isme website ke features aur navigation ka zikr hai.")

col1, col2 = st.columns(2):
Do columns create karta hai jisse content ko horizontal divide kiya ja sake.
("Columns se content ko do hisso me divide karke display kiya jata hai.")

with col1:
Is block me jo bhi likha gaya hai, woh pehle column me display hoga.

st.header("Features"):
Pehle column me "Features" header display karta hai.

st.write(""" ... """):
Features ki list jisme interactive data analysis, visualizations, etc. bataya gaya hai.

with col2:
Dusre column ke liye block.

st.header("Get Started"):
Dusre column me "Get Started" header display karta hai.

st.write(""" ... """):
User ko guide karta hai ke sidebar se kisi page ko select kare.

5. Data Analysis Page
python
Copy
Edit
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
elif page == "Data Analysis":
Agar selected page "Data Analysis" hai, yeh block execute hoga.

st.title("Data Analysis 📊"):
Page ka title set karta hai "Data Analysis" ke sath, aur ek emoji bhi show karta hai.

data = pd.DataFrame({...}):
Yeh block sample data generate karta hai:

'x': np.random.randn(100):
100 random numbers normally distributed.

'y': np.random.randn(100):
100 random numbers normally distributed.

'category': np.random.choice(['A', 'B', 'C'], 100):
Randomly 100 values choose karta hai category A, B, ya C me se. ("Is se ek DataFrame create hota hai jisme numerical aur categorical data hai.")

st.write("### Sample Data"):
Yeh heading display karta hai jo sample data ko denote karta hai.

st.dataframe(data):
DataFrame ko interactive table format me display karta hai.

st.write("### Data Summary"):
Yeh heading display karta hai summary ke liye.

st.write(data.describe()):
Data ka statistical summary (mean, std, quartiles, etc.) dikhata hai using Pandas' describe() function. ("Yeh section data ka analysis aur summary provide karta hai.")

6. Visualization Page
python
Copy
Edit
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
elif page == "Visualization":
Jab user "Visualization" page select kare.

st.title("Data Visualization 📈"):
Page ka title set karta hai jo visualization pe focused hai.

data = pd.DataFrame({...}):
Yahan phir se sample data create ho raha hai, jo upar wale Data Analysis page jaisa hi hai.

fig = px.scatter(data, x='x', y='y', color='category', title='Interactive Scatter Plot'):
Plotly Express ka scatter plot generate karta hai:

x='x' aur y='y':
Data ke x aur y columns ko plot ke liye use karta hai.

color='category':
Alag alag categories ke hisaab se points ko rang deta hai.

title='Interactive Scatter Plot':
Chart ka title set karta hai. ("Interactive scatter plot se data points ko visual form me represent kiya jata hai.")

st.plotly_chart(fig, use_container_width=True):
Generated plot ko Streamlit app me display karta hai aur container ki puri width ka istemal karta hai.

7. About Page
python
Copy
Edit
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
elif page == "About":
Jab user "About" page select kare, yeh block execute hoga.

st.title("About This Website ℹ️"):
Page ka title show karta hai jisme website ke bare me brief info di gayi hai.

st.write(""" ... """):
Multi-line string me website ke creation aur use hui technologies ko detail se bataya gaya hai:

"Technologies Used":

Streamlit

Pandas

NumPy

Plotly

"Features":

Multi-page navigation

Interactive data analysis

Beautiful visualizations

Responsive design
("Is section me website ke background, istemal hui technologies, aur uske features ke bare me bataya gaya hai.")

Summary
Yeh code ek multi-page Streamlit website banata hai jisme:

Sidebar navigation: Jo different pages (Home, Data Analysis, Visualization, About) me navigate karne ke liye options deta hai.

Home page: Welcome message aur site features dikhata hai.

Data Analysis page: Sample data create karta hai, uska interactive table aur statistical summary dikhata hai.

Visualization page: Interactive scatter plot create karke data visualization provide karta hai.

About page: Website ke bare me detailed information aur use hui technologies ko explain karta hai.

