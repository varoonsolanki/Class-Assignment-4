# my_website.py

import streamlit as st
import smtplib
from email.message import EmailMessage
import os

# Page config
st.set_page_config(page_title="My Streamlit Website", layout="wide")

# Sidebar Navigation
st.sidebar.title("🔗 Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Contact"])

# Dark mode toggle
dark_mode = st.sidebar.checkbox("🌙 Dark Mode")

if dark_mode:
    st.markdown("""
        <style>
        body { background-color: #1e1e1e; color: white; }
        .stApp { background-color: #1e1e1e; color: white; }
        </style>
    """, unsafe_allow_html=True)

# Home Page
if page == "Home":
    st.title("🏠 Welcome to My Streamlit Website")
    
    # Header with larger text
    st.markdown("""
        ## Hello! I'm Varoon 👋
        I'm a **Python Developer**, **AI Enthusiast**, and **Student at GIAIC**.  
        I love creating **useful tools** and **innovative projects**. Here's a sneak peek into my world.
    """)

    # Introduction
    st.write("""
        I specialize in developing **web apps**, **AI bots**, and more using:
        - **Streamlit** for quick web apps
        - **Python** for automation and AI
        - **React/Next.js** for dynamic web development
        - **Neural Networks** for smart predictions
    """)

    # Showcase 1 or 2 projects
    st.subheader("🚀 Featured Projects")
    
    st.write("""
        ### 🎲 **Guess the Number Game**
        A fun and simple number guessing game with a twist. Can you guess the secret number in the least tries?
    """)
    st.image("https://picsum.photos/500/300?random=1", caption="Guess the Number Game", use_column_width=True)

    st.write("""
        ### 🧮 **BMI Calculator**
        A health-focused app that calculates your **BMI** and gives a quick status about your health range. It even saves your results for future reference!
    """)
    st.image("https://picsum.photos/500/300?random=2", caption="BMI Calculator", use_column_width=True)

    # Call to action buttons
    st.write("---")
    st.markdown("""
        Want to know more?  
        - [About Me](#about)
        - [Contact Me](#contact)
    """)
    
    st.success("Let's build something amazing together!")

# About Page
elif page == "About":
    st.title("👨‍💻 About Me")
    st.write("""
        Hi! I'm Varoon, a passionate Python developer and student at GIAIC.  
        I love building fun and useful projects like:
        - 🔢 Unit Converters  
        - 🤖 Prediction Bots  
        - 🧠 AI Tools  
        - 🌐 Streamlit Websites  

        Thanks for visiting my site!
    """)
    st.info("Skills: Python, React, Next.js, Streamlit")

# Projects Page
elif page == "Projects":
    st.title("🚀 My Projects")
    st.markdown("""
    - 🧮 **BMI Calculator** – Health-focused Streamlit app with chart & data save.
    - 🎲 **Guess the Number** – Fun logic-based number guessing game.
    - ✂️ **Rock Paper Scissors** – Classic user vs computer game.
    - ⏳ **Countdown Timer** – Simple timer with real-time updates.
    - 🔐 **Password Generator** – Strong & random password creator.
    - 🧠 **WinGo Prediction Bot** – AI-based predictor for trend-based games.
    """)

# Contact Page
elif page == "Contact":
    st.title("📞 Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send")

        if submit:
            # Fake email logic (commented out for local use)
            # msg = EmailMessage()
            # msg.set_content(f"From: {name}\nEmail: {email}\nMessage:\n{message}")
            # msg['Subject'] = "New Contact Form Message"
            # msg['From'] = email
            # msg['To'] = "your@email.com"

            # Send email (use real credentials & uncomment below to enable)
            # with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            #     smtp.starttls()
            #     smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
            #     smtp.send_message(msg)

            st.success(f"Thanks {name}! Your message has been received. 📬")
