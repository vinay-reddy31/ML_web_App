# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 20:56:24 2023

@author: vinay
"""

import numpy as np
import pickle
import streamlit as st

# Load the saved model
loaded_model = pickle.load(open('C:/Users/vinay/OneDrive/Desktop/ML Project/ML web/trained_model.sav', 'rb'))

# Create a function for prediction
def kidney_prediction(new_data):
   input_data_as_numpy_array = np.asarray(new_data, dtype=float)  # Convert to float
   input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
   predictions = loaded_model.predict(input_data_reshaped)
   if predictions[0] == 0:
       return "No Kidney Disease"
   else:
       return "Seems like Kidney Disease. Please Contact Doctor!"

def main():
    st.title('Chronic Kidney Disease Prediction Web App')
    st.write("yes:1, No:0")

    # Get input data from the user
    col1,col2,col3=st.columns(3)
    
    with col1:
        age = st.text_input('Age',)
    with col2:
        blood_pressure = st.text_input('Blood Pressure',)
    
    with col3:
        specific_gravity = st.text_input('Specific Gravity', )
        
    with col1:
        red_blood_cells = st.text_input('Red Blood Cells (1 or 0)', value=0)
    with col2:
        pus_cell = st.text_input('Pus Cell (1 or 0)', value=0)
    with col3:
        pus_cell_clumps = st.text_input('Pus Cell Clumps (1 or 0)', value=0)
    
    with col1:
        bacteria = st.text_input('Bacteria (1 or 0)', value=0)
    with col2:
        blood_glucose_random = st.text_input('Blood Glucose')
    with col3:
        blood_urea = st.text_input('Blood Urea')
        
    with col1:
        serum_creatinine = st.text_input('Serum Creatinine')
    with col2:
        sodium = st.text_input('Sodium')
    with col3:
        potassium = st.text_input('Potassium')
        
    with col1:
        haemoglobin = st.text_input('Haemoglobin')
    with col2:
        hypertension = st.text_input('Hypertension (1 or 0)', value=0)
    with col3:
        appetite = st.text_input('Appetite (1 or 0)', value=0)
        
    with col1:
        peda_edema = st.text_input('Peda Edema (1 or 0)', value=0)
    with col2:
        anemia = st.text_input('Anemia (1 or 0)', value=0)
    
    diagnosis = ''

    # Create a button for prediction
    if st.button('Test Result'):
        try:
            # Convert user input to float and pass it to the prediction function
            input_data = [
                float(age), float(blood_pressure), float(specific_gravity),
                float(red_blood_cells), float(pus_cell), float(pus_cell_clumps),
                float(bacteria), float(blood_glucose_random), float(blood_urea),
                float(serum_creatinine), float(sodium), float(potassium),
                float(haemoglobin), float(hypertension), float(appetite),
                float(peda_edema), float(anemia)
            ]
            diagnosis = kidney_prediction(input_data)
        except ValueError:
            diagnosis = "Invalid input. Please enter numeric values."

    st.success(diagnosis)

if __name__ == '__main__':
    main()
