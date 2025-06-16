import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('Gradient_boosting.pkl', 'rb'))

# Set background image with blur and low opacity
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = image.read()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded.encode('base64').decode()}");
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
            opacity: 0.85;
            filter: blur(2px);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply background (comment below line if you don’t have image)
# add_bg_from_local("car_bg.jpg")

# Reapply foreground content with clean layout
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

# Input fields
present_price = st.number_input('Present Price (in lakhs)', min_value=0.0, format="%.2f")
kms_driven = st.number_input('Kms Driven', min_value=0)
owner = st.selectbox('Number of Previous Owners', [0, 1, 2, 3])
years_old = st.number_input('Number of Years Old', min_value=0)

# One-hot encoded fields
fuel_type_diesel = st.selectbox('Fuel Type: Is it Diesel?', ['No', 'Yes'])
fuel_type_petrol = st.selectbox('Fuel Type: Is it Petrol?', ['No', 'Yes'])
seller_individual = st.selectbox('Seller Type: Individual?', ['No', 'Yes'])
transmission_manual = st.selectbox('Transmission: Manual?', ['No', 'Yes'])

# Convert categorical to binary
fuel_type_diesel = 1 if fuel_type_diesel == 'Yes' else 0
fuel_type_petrol = 1 if fuel_type_petrol == 'Yes' else 0
seller_individual = 1 if seller_individual == 'Yes' else 0
transmission_manual = 1 if transmission_manual == 'Yes' else 0

# Prediction
if st.button("Predict Selling Price"):
    input_features = np.array([[present_price, kms_driven, owner, years_old,
                                fuel_type_diesel, fuel_type_petrol,
                                seller_individual, transmission_manual]])
    
    result = model.predict(input_features)[0]
    st.success(f"🚘 Estimated Selling Price: ₹{result:.2f} lakhs")

st.markdown("</div>", unsafe_allow_html=True)
