import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("svm_model.pkl")

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .stButton>button {
        background-color: #00FFAA;
        color: black;
        border-radius: 10px;
        font-size: 18px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stNumberInput>div>div>input {
        background-color: #262730;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Logo dan Judul
col1, col2 = st.columns([1,4])
with col1:
    st.image("logo.png", width=80)  # ganti dengan logo kamu
with col2:
    st.title("Prediksi Kanker Payudara")
st.write("Masukkan nilai fitur dari data pasien")

# Layout input (2 kolom)
col1, col2 = st.columns(2)

with col1:
    radius_mean = st.number_input("Mean Radius", min_value=0.0, step=0.01)
    texture_mean = st.number_input("Mean Texture", min_value=0.0, step=0.01)
    perimeter_mean = st.number_input("Mean Perimeter", min_value=0.0, step=0.1)

with col2:
    area_mean = st.number_input("Mean Area", min_value=0.0, step=1.0)
    smoothness_mean = st.number_input("Mean Smoothness", min_value=0.0, step=0.001)

# Dummy fitur lainnya (total 30 fitur)
features = [radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean] + [0]*25

# Tombol Prediksi
if st.button("🚀 Prediksi"):
    prediction = model.predict([np.array(features)])[0]
    prob = model.predict_proba([np.array(features)])[0]

    st.subheader("Hasil Prediksi:")
    if prediction == 1:
        st.success(f"🟢 Jinak (Probabilitas: {prob[1]*100:.2f}%)")
    else:
        st.error(f"🔴 Ganas (Probabilitas: {prob[0]*100:.2f}%)")
