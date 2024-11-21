# Random Forest pkl file

import streamlit as st
import joblib
import pandas as pd


# Load the model

model=joblib.load('Production Defect Status.pkl')



# Title to App
st.title('Production Defect Status')


# Input Fields
production_volume = st.number_input('Production Volume ')
production_cost = st.number_input('Production Cost (Rs) ')
supplier_quality = st.number_input('Supplier Quality ')
defect_rate = st.number_input('Defect Rate ')
quality_score = st.number_input('QualityScore ')
maintenance_hours = st.number_input('Maintenance Hours ')
additive_material_cost = st.number_input('Additive Material Cost (Rs)')

# Creating a DataFrame
input_data = pd.DataFrame(

    {
        'ProductionVolume':[production_volume],
        'ProductionCost':[production_cost],
        'SupplierQuality':[supplier_quality],
        'DefectRate':[defect_rate],
        'QualityScore':[quality_score],
        'MaintenanceHours':[maintenance_hours],
        'AdditiveMaterialCost':[additive_material_cost]

    }
)


if st.button('Predict'):
    DefectStatus = model.predict(input_data).item()
    st.write(f"Manufacturing Defect: {DefectStatus}")
