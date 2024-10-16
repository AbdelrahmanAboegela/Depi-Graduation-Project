import streamlit as st
import numpy as np
import joblib


model_female = joblib.load('model_Female.h5')
model_male = joblib.load('model_Male.h5')


st.title("Stress Classification")

gender = st.selectbox("Select Gender:", ["Male", "Female"])

data_input = st.text_area("Enter the 79 numeric features as a space-separated row:")

if st.button("Classify"):
    if data_input:
        try:
            input_features = [float(value.strip()) for value in data_input.split() if value.strip()]

            if len(input_features) != 79:
                st.error("Please enter exactly 79 features.")
            else:
                input_data = np.array(input_features).reshape(1, 1, 79)

                if gender == "Male":
                    prediction = model_male.predict(input_data)
                else:
                    prediction = model_female.predict(input_data)

                st.write(f"Classification result: {prediction[0][0]}")
        except ValueError:
            st.error("Please enter valid numeric values.")
