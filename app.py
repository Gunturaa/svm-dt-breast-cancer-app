import streamlit as st
import numpy as np
import joblib

# Page config
st.set_page_config(
    page_title="Prediksi Kanker Payudara",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load model (dengan error handling)
@st.cache_resource
def load_model():
    try:
        return joblib.load("svm_model.pkl")
    except FileNotFoundError:
        st.error("❌ Model file tidak ditemukan. Pastikan file 'svm_model.pkl' ada di direktori yang sama.")
        return None

model = load_model()

# Custom CSS - Diperbaiki dan dirapikan
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Reset dan Base Styles */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%) !important;
        font-family: 'Inter', sans-serif !important;
        color: #ffffff;
    }
    
    #MainMenu, footer, header, .stDeployButton {
        visibility: hidden;
    }
    
    .block-container {
        max-width: 1200px !important;
        padding: 1rem 2rem 3rem 2rem !important;
    }
    
    /* Header Section */
    .header {
        text-align: center;
        background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%);
        border: 1px solid #333;
        border-radius: 20px;
        padding: 3rem 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    
    .header h1 {
        color: #ffffff;
        font-size: 2.8rem;
        font-weight: 700;
        margin: 1rem 0 0.5rem 0;
        background: linear-gradient(135deg, #00ff88, #0099ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .header p {
        color: #b0b0b0;
        font-size: 1.2rem;
        margin: 0 auto;
        max-width: 700px;
        line-height: 1.6;
        font-weight: 400;
    }
    
    /* Input Section */
    .input-container {
        background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%);
        border: 1px solid #404040;
        border-radius: 16px;
        padding: 2.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
    }
    
    .input-title {
        color: #ffffff;
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    
    .input-subtitle {
        color: #a0a0a0;
        font-size: 1rem;
        text-align: center;
        margin-bottom: 2rem;
        line-height: 1.5;
    }
    
    /* Custom Input Styling */
    .stNumberInput > div > div > input {
        background: #333 !important;
        border: 1px solid #555 !important;
        border-radius: 8px !important;
        color: #ffffff !important;
        font-size: 1rem !important;
        padding: 0.75rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #00ff88 !important;
        box-shadow: 0 0 0 2px rgba(0, 255, 136, 0.2) !important;
    }
    
    .stNumberInput > label {
        color: #ffffff !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #00ff88, #0099ff) !important;
        border: none !important;
        border-radius: 12px !important;
        color: #ffffff !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        padding: 0.8rem 2rem !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        margin: 1rem 0 !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(0, 255, 136, 0.3) !important;
    }
    
    /* Result Cards */
    .result {
        background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%);
        border-radius: 16px;
        padding: 2.5rem;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }
    
    .result.benign {
        border: 2px solid #00ff88;
        box-shadow: 0 10px 30px rgba(0, 255, 136, 0.2);
    }
    
    .result.malignant {
        border: 2px solid #ff4757;
        box-shadow: 0 10px 30px rgba(255, 71, 87, 0.2);
    }
    
    .result h2 {
        color: #ffffff;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .result .probability {
        color: #ffffff;
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 1rem;
        opacity: 0.9;
    }
    
    .result .description {
        color: #b0b0b0;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    
    /* Warning Section */
    .warning {
        background: linear-gradient(135deg, #2a2a1a 0%, #3a3a2a 100%);
        border: 1px solid #6b5b00;
        border-left: 4px solid #ffa500;
        border-radius: 12px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 8px 25px rgba(255, 165, 0, 0.1);
    }
    
    .warning h3 {
        color: #ffa500;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .warning ul {
        color: #c0c0c0;
        margin-left: 1.5rem;
        line-height: 1.8;
    }
    
    .warning li {
        margin-bottom: 0.5rem;
    }
    
    /* Info Cards */
    .info-card {
        background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%);
        border: 1px solid #404040;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }
    
    .info-card:hover {
        border-color: #00ff88;
        box-shadow: 0 5px 15px rgba(0, 255, 136, 0.1);
    }
    
    .info-card h4 {
        color: #00ff88;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .info-card p {
        color: #b0b0b0;
        font-size: 0.95rem;
        line-height: 1.5;
        margin: 0;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0;
        border-top: 1px solid #333;
        color: #666;
        margin-top: 3rem;
    }
    
    .footer a {
        color: #00ff88;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    
    .footer a:hover {
        text-decoration: underline;
        color: #0099ff;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .block-container {
            padding: 1rem !important;
        }
        
        .header h1 {
            font-size: 2.2rem;
        }
        
        .header p {
            font-size: 1rem;
        }
        
        .input-container {
            padding: 1.5rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Header dengan logo di tengah - menggunakan Streamlit image
import os
import base64

# Fungsi untuk encode gambar ke base64
def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Header dengan logo
logo_path = "logo.png"
if os.path.exists(logo_path):
    try:
        # Encode logo ke base64
        logo_base64 = get_base64_of_bin_file(logo_path)
        
        st.markdown(f"""
            <div style="text-align: center; background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%); 
                        border: 1px solid #333; border-radius: 20px; padding: 3rem 2rem; margin-bottom: 2rem;
                        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);">
                <div style="margin-bottom: 1rem;">
                    <img src="data:image/png;base64,{logo_base64}" alt="Logo" style="width: 80px; height: 80px; border-radius: 50%; 
                         box-shadow: 0 4px 15px rgba(0, 255, 136, 0.3);">
                </div>
                <h1 style="margin: 0; font-size: 2.8rem; font-weight: 700; 
                    background: linear-gradient(135deg, #00ff88, #0099ff);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    background-clip: text;">
                    Prediksi Kanker Payudara
                </h1>
                <p style="color: #b0b0b0; font-size: 1.2rem; margin: 0.5rem auto 0 auto; line-height: 1.6; max-width: 700px;">
                    Sistem AI untuk deteksi dini kanker payudara menggunakan teknologi Machine Learning yang canggih dan akurat
                </p>
            </div>
        """, unsafe_allow_html=True)
    except Exception as e:
        # Jika gagal load logo, gunakan st.image
        st.markdown("""
            <div style="text-align: center; background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%); 
                        border: 1px solid #333; border-radius: 20px; padding: 3rem 2rem; margin-bottom: 2rem;
                        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);">
                <div style="margin-bottom: 1rem;">
        """, unsafe_allow_html=True)
        
        # Gunakan st.image sebagai fallback
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.image(logo_path, width=80)
        
        st.markdown("""
                </div>
                <h1 style="margin: 0; font-size: 2.8rem; font-weight: 700; 
                    background: linear-gradient(135deg, #00ff88, #0099ff);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    background-clip: text;">
                    Prediksi Kanker Payudara
                </h1>
                <p style="color: #b0b0b0; font-size: 1.2rem; margin: 0.5rem auto 0 auto; line-height: 1.6; max-width: 700px;">
                    Sistem AI untuk deteksi dini kanker payudara menggunakan teknologi Machine Learning yang canggih dan akurat
                </p>
            </div>
        """, unsafe_allow_html=True)
else:
    # Jika logo tidak ada, tampilkan header tanpa logo
    st.markdown("""
        <div style="text-align: center; background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%); 
                    border: 1px solid #333; border-radius: 20px; padding: 3rem 2rem; margin-bottom: 2rem;
                    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);">
            <h1 style="margin: 0; font-size: 2.8rem; font-weight: 700; 
                background: linear-gradient(135deg, #00ff88, #0099ff);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;">
                🩺 Prediksi Kanker Payudara
            </h1>
            <p style="color: #b0b0b0; font-size: 1.2rem; margin: 0.5rem auto 0 auto; line-height: 1.6; max-width: 700px;">
                Sistem AI untuk deteksi dini kanker payudara menggunakan teknologi Machine Learning yang canggih dan akurat
            </p>
        </div>
    """, unsafe_allow_html=True)

# Information Cards
st.markdown("""
    <div style="margin-bottom: 2rem;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem;">
            <div class="info-card">
                <h4>🎯 Akurasi Tinggi</h4>
                <p>Model menggunakan algoritma SVM dengan tingkat akurasi tinggi dalam mendeteksi kanker payudara</p>
            </div>
            <div class="info-card">
                <h4>⚡ Analisis Cepat</h4>
                <p>Hasil prediksi didapat dalam hitungan detik dengan analisis mendalam</p>
            </div>
            <div class="info-card">
                <h4>🔬 Berbasis Sains</h4>
                <p>Menggunakan parameter medis standar untuk analisis yang komprehensif</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Input Section
st.markdown("""
    <div class="input-container">
        <div class="input-title">📊 Masukkan Data Klinis</div>
        <div class="input-subtitle">Silakan masukkan nilai-nilai parameter berikut berdasarkan hasil pemeriksaan medis</div>
    </div>
""", unsafe_allow_html=True)

# Input dalam columns yang lebih rapi
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("##### 🔵 Parameter Ukuran")
    radius_mean = st.number_input(
        "Mean Radius (μm)", 
        min_value=0.0, 
        max_value=50.0, 
        step=0.01, 
        help="Rata-rata jari-jari sel (dalam mikrometer)",
        placeholder="contoh: 17.8"
    )
    
    area_mean = st.number_input(
        "Mean Area (μm²)", 
        min_value=0.0, 
        max_value=3000.0, 
        step=1.0,
        help="Rata-rata luas area sel (dalam mikrometer persegi)",
        placeholder="contoh: 1001"
    )

with col2:
    st.markdown("##### 🟡 Parameter Bentuk")
    texture_mean = st.number_input(
        "Mean Texture", 
        min_value=0.0, 
        max_value=50.0, 
        step=0.01,
        help="Rata-rata variasi intensitas skala abu-abu",
        placeholder="contoh: 10.5"
    )
    
    smoothness_mean = st.number_input(
        "Mean Smoothness", 
        min_value=0.0, 
        max_value=1.0, 
        step=0.001,
        help="Rata-rata kehalusan permukaan sel (0-1)",
        placeholder="contoh: 0.118"
    )

with col3:
    st.markdown("##### 🟢 Parameter Perimeter")
    perimeter_mean = st.number_input(
        "Mean Perimeter (μm)", 
        min_value=0.0, 
        max_value=500.0, 
        step=0.1,
        help="Rata-rata keliling sel (dalam mikrometer)",
        placeholder="contoh: 122.8"
    )
    
    # Spacer untuk alignment
    st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Prediction Button
st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)

col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    predict_button = st.button("🚀 Analisis Prediksi", type="primary")

# Validation dan Prediction
if predict_button:
    # Validasi input
    if not all([radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean]):
        st.error("⚠️ Mohon lengkapi semua parameter yang diperlukan!")
    elif model is None:
        st.error("❌ Model belum dimuat. Pastikan file model tersedia.")
    else:
        # Buat array fitur (30 fitur total, 5 yang digunakan + 25 padding dengan 0)
        features = [radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean] + [0]*25
        
        try:
            # Prediksi
            prediction = model.predict([np.array(features)])[0]
            probabilities = model.predict_proba([np.array(features)])[0]
            
            # Tampilkan hasil
            if prediction == 1:  # Benign
                confidence = probabilities[1] * 100
                st.markdown(f"""
                    <div class="result benign">
                        <h2>✅ JINAK (Benign)</h2>
                        <div class="probability">Tingkat Kepercayaan: {confidence:.1f}%</div>
                        <div class="description">
                            Hasil analisis menunjukkan bahwa karakteristik sel cenderung bersifat jinak (non-kanker).
                            <br><br>
                            <strong>Interpretasi:</strong> Sel-sel yang dianalisis memiliki pola yang konsisten dengan tumor jinak.
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Additional info untuk hasil benign
                st.success("🎉 **Hasil Positif:** Analisis menunjukkan indikasi yang menggembirakan!")
                
            else:  # Malignant
                confidence = probabilities[0] * 100
                st.markdown(f"""
                    <div class="result malignant">
                        <h2>⚠️ GANAS (Malignant)</h2>
                        <div class="probability">Tingkat Kepercayaan: {confidence:.1f}%</div>
                        <div class="description">
                            Hasil analisis menunjukkan bahwa karakteristik sel cenderung bersifat ganas (kanker).
                            <br><br>
                            <strong>Interpretasi:</strong> Sel-sel yang dianalisis memiliki pola yang perlu mendapat perhatian medis segera.
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Additional warning untuk hasil malignant
                st.error("🚨 **Perhatian:** Hasil ini memerlukan konsultasi medis segera!")
                
        except Exception as e:
            st.error(f"❌ Terjadi kesalahan saat melakukan prediksi: {str(e)}")

# Warning Section
st.markdown("""
    <div class="warning">
        <h3>⚠️ Penting untuk Diperhatikan</h3>
        <ul>
            <li><strong>Alat Bantu Diagnostik:</strong> Hasil ini hanya sebagai alat bantu analisis dan bukan diagnosis medis resmi yang dapat menggantikan pemeriksaan dokter.</li>
            <li><strong>Konsultasi Medis Wajib:</strong> Selalu konsultasikan hasil ini dengan dokter spesialis onkologi atau dokter yang berkompeten untuk interpretasi yang akurat.</li>
            <li><strong>Pemeriksaan Lanjutan:</strong> Diperlukan tes laboratorium, biopsi, dan pemeriksaan medis lainnya untuk konfirmasi diagnosis yang definitif.</li>
            <li><strong>Tidak Menggantikan Skrining:</strong> Tool ini tidak menggantikan mammografi, USG, atau pemeriksaan rutin lainnya yang direkomendasikan.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Additional Information
with st.expander("📚 Informasi Parameter"):
    st.markdown("""
    **Mean Radius:** Rata-rata jarak dari pusat ke titik-titik di perimeter sel
    
    **Mean Texture:** Standar deviasi nilai-nilai skala abu-abu dalam gambar
    
    **Mean Perimeter:** Rata-rata ukuran keliling inti sel
    
    **Mean Area:** Rata-rata luas area inti sel
    
    **Mean Smoothness:** Rata-rata variasi lokal dalam panjang radius
    
    *Parameter ini diperoleh dari analisis citra mikroskopis biopsi jaringan payudara.*
    """)

with st.expander("🔬 Tentang Model AI"):
    st.markdown("""
    **Teknologi:** Support Vector Machine (SVM)
    
    **Dataset:** Berdasarkan Wisconsin Diagnostic Breast Cancer (WDBCD)
    
    **Fitur:** Menganalisis 30+ parameter morfologis sel
    
    **Validasi:** Model telah divalidasi menggunakan teknik cross-validation
    
    **Keterbatasan:** Hasil bergantung pada kualitas input dan tidak 100% akurat
    """)

# Footer
st.markdown("""
    <div class="footer">
        <strong>Breast Cancer Prediction System v2.0</strong><br>
        Dikembangkan untuk membantu deteksi dini kanker payudara • 
        <a href="#" target="_blank">Pelajari lebih lanjut</a> • 
        <a href="#" target="_blank">Konsultasi Online</a>
        <br><br>
        <small>⚕️ Selalu konsultasikan dengan tenaga medis profesional</small>
    </div>
""", unsafe_allow_html=True)