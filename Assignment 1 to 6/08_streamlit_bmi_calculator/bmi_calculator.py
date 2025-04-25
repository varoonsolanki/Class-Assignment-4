import matplotlib.pyplot as plt
import streamlit as st 
import pandas as pd
import time

# Page config
st.set_page_config(page_title="BMI Calculator", page_icon="🧮", layout="centered")

# App Title
st.title("🧮 BMI Calculator")
st.markdown("""
<style>
.big-font {
    font-size:28px !important;
    font-weight:600;
    color:#4CAF50;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state for saving
if 'bmi_records' not in st.session_state:
    st.session_state['bmi_records'] = []

# Gender Selection
col1, col2 = st.columns(2)
with col1:
    gender = st.radio("Select Gender:", ["Male ♂", "Female ♀"])

# Inputs
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)
height_cm = st.number_input("Enter your height (cm):", min_value=1.0, step=0.1)

# Calculate BMI
if weight and height_cm:
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    
    st.markdown(f"<p class='big-font'>📊 Your BMI is: {bmi:.2f}</p>", unsafe_allow_html=True)

    # BMI Category
    if bmi < 18.5:
        status = "Underweight"
        st.warning("⚠️ You are underweight")
    elif 18.5 <= bmi < 24.9:
        status = "Normal"
        st.success("✅ You are in the normal weight range")
    elif 25 <= bmi < 29.9:
        status = "Overweight"
        st.info("ℹ️ You are overweight")
    else:
        status = "Obese"
        st.error("❌ You are obese")

    # Save result
    if st.button("💾 Save Result"):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        st.session_state['bmi_records'].append({
            "Time": timestamp,
            "Gender": gender,
            "Weight (kg)": weight,
            "Height (cm)": height_cm,
            "BMI": round(bmi, 2),
            "Status": status
        })
        st.success("Result saved!")

# Show saved records
if st.session_state['bmi_records']:
    st.subheader("📁 Saved BMI Records")
    df = pd.DataFrame(st.session_state['bmi_records'])
    st.dataframe(df, use_container_width=True)

    # BMI Trend Chart
    st.subheader("📈 BMI History Chart")
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['BMI'], marker='o', linestyle='-', color='blue')
    ax.set_xlabel("Time")
    ax.set_ylabel("BMI")
    ax.set_title("BMI Over Time")
    ax.grid(True)
    plt.xticks(rotation=45)
    st.pyplot(fig)
else:
    st.info("No records saved yet.")
