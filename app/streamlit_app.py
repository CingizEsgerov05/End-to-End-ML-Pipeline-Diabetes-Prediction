import streamlit as st
import requests

# PAGE CONFIG
st.set_page_config(page_title="Diabetes Prediction", page_icon="🧬", layout="wide")

# HEADER
st.markdown("""
    <h1 style='text-align: center; color: #4A90E2; margin-bottom: 5px;'>
        🧬 Diabetes Risk Prediction
    </h1>
    <p style='text-align: center; font-size: 17px; color: #666; margin-top: -10px;'>
        Enter patient information to estimate diabetes risk using a Machine Learning model.
    </p>
""", unsafe_allow_html=True)

st.write("")

# MAIN LAYOUT (Two Columns)
left, right = st.columns([2, 1])  # left larger, right smaller for prediction


# ------------------ LEFT SECTION (INPUT FORM) ------------------
with left:

    st.markdown("### 🩺 Patient Medical Information")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, value=30, step=1)
        bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=22.5, step=0.1)
        s1 = st.number_input("S1 (Cholesterol)", value=150.0)

    with col2:
        sex_choice = st.selectbox("Sex", ["Male", "Female"])
        sex = 1 if sex_choice == "Male" else 0
        bp = st.number_input("Blood Pressure", min_value=40, max_value=200, value=80, step=1)
        s2 = st.number_input("S2 (LDL)", value=100.0)

    col3, col4, col5 = st.columns(3)

    with col3:
        s3 = st.number_input("S3 (HDL)", value=50.0)
    with col4:
        s4 = st.number_input("S4 (TCH ratio)", value=3.0)
    with col5:
        s5 = st.number_input("S5 (LTG — log triglycerides)", value=4.0)

    s6 = st.number_input("S6 (Blood Sugar Level)", value=90.0)

    st.write("")
    predict_btn = st.button("🔍 Predict Diabetes Risk")


# ------------------ RIGHT SECTION (PREDICTION PANEL) ------------------
with right:

    st.markdown("""
        <div style='padding: 20px; border-radius: 15px; background-color: #f9f9f9;
                    box-shadow: 0px 3px 10px rgba(0,0,0,0.07);'>
            <h3 style='text-align:center; color:#4A90E2;'>Prediction Result</h3>
            <p style='text-align:center; color:#777; margin-top:-10px;'>Model output will appear here</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("")

    if predict_btn:

        features = [age, sex, bmi, bp, s1, s2, s3, s4, s5, s6]

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json={"data": features}
        )

        result = response.json()

        st.write("")  # spacing

        # RESULT CARD
        if "prediction" in result:
            pred = result["prediction"]

            if pred == 1:
                st.markdown("""
                    <div style='padding: 25px; background-color:#ffe6e6; border-radius:15px;
                                text-align:center; box-shadow:0 3px 10px rgba(0,0,0,0.05);'>
                        <h2 style='color:#D9534F;'>🔴 High Diabetes Risk</h2>
                        <p style='color:#444;'>The model indicates a high probability of diabetes.</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div style='padding: 25px; background-color:#e9ffe9; border-radius:15px;
                                text-align:center; box-shadow:0 3px 10px rgba(0,0,0,0.05);'>
                        <h2 style='color:#5CB85C;'>🟢 Low Diabetes Risk</h2>
                        <p style='color:#444;'>The model indicates a low probability of diabetes.</p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.error("API Error: " + str(result))
