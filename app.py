import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('XGBoosting.pkl', 'rb'))

# Optional: Background styling (keep commented if unused)
# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image:
#         encoded = image.read()
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url("data:image/jpeg;base64,{encoded.encode('base64').decode()}");
#             background-size: cover;
#             background-attachment: fixed;
#             background-repeat: no-repeat;
#             opacity: 0.85;
#             filter: blur(2px);
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )
# add_bg_from_local("car_bg.jpg")

# Main layout styling
st.markdown(
    """
    <style>
    .main-container {
        position: relative;
        z-index: 10;
    }
    </style>
    """, unsafe_allow_html=True
)
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

st.title("🚗 Car Selling Price Predictor")

# Input fields matching your model's expected input
present_price = st.number_input('Present Price (in lakhs)', min_value=0.0, format="%.2f")
kms_driven = st.number_input('Kms Driven', min_value=0)
owner = st.selectbox('Number of Previous Owners', [0, 1, 2, 3])
years_old = st.number_input('Number of Years Old', min_value=0)

# Checkboxes for boolean (already encoded) features
fuel_type_diesel = st.checkbox('Fuel Type: Diesel')
fuel_type_petrol = st.checkbox('Fuel Type: Petrol')
seller_individual = st.checkbox('Seller Type: Individual')
transmission_manual = st.checkbox('Transmission: Manual')

# Prediction
if st.button("Predict Selling Price"):
    input_features = np.array([[present_price, kms_driven, owner, years_old,
                                fuel_type_diesel, fuel_type_petrol,
                                seller_individual, transmission_manual]])
    
    result = model.predict(input_features)[0]
    st.success(f"🚘 Estimated Selling Price: ₹{result:.2f} lakhs")

st.markdown("</div>", unsafe_allow_html=True)
