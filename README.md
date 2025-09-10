# 🩺 Breast Cancer Prediction System

Sistem prediksi kanker payudara berbasis AI menggunakan teknologi Machine Learning yang canggih dan akurat untuk membantu deteksi dini kanker payudara.

## 📋 Deskripsi

Aplikasi web ini menggunakan algoritma **Support Vector Machine (SVM)** untuk menganalisis parameter klinis dan memberikan prediksi apakah sel payudara bersifat jinak (benign) atau ganas (malignant). Sistem ini dikembangkan menggunakan Streamlit dengan antarmuka yang modern dan user-friendly.

## ✨ Fitur Utama

- 🎯 **Akurasi Tinggi**: Menggunakan algoritma SVM dengan tingkat akurasi tinggi
- ⚡ **Analisis Cepat**: Hasil prediksi didapat dalam hitungan detik
- 🔬 **Berbasis Sains**: Menggunakan parameter medis standar untuk analisis komprehensif
- 🎨 **UI Modern**: Antarmuka yang responsif dengan desain dark theme yang elegan
- 📱 **Responsive Design**: Dapat diakses dari berbagai perangkat

## 🌐 Demo Online

Aplikasi ini dapat diakses secara online tanpa perlu instalasi:

**🔗 [https://predictionsbreastcancer.streamlit.app/](https://predictionsbreastcancer.streamlit.app/)**

Cukup klik link di atas untuk langsung mencoba aplikasi prediksi kanker payudara secara online!

## 🚀 Cara Menjalankan Aplikasi Lokal

### Prerequisites

Pastikan Anda telah menginstall Python 3.7 atau versi yang lebih baru.

### Instalasi

1. **Clone atau download repository ini**
   ```bash
   git clone <repository-url>
   cd breast_cancer_app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Pastikan file model tersedia**
   - `svm_model.pkl` - Model SVM yang telah dilatih
   - `dt_model.pkl` - Model Decision Tree (opsional)
   - `logo.png` - Logo aplikasi (opsional)

4. **Jalankan aplikasi**
   ```bash
   streamlit run app.py
   ```

5. **Buka browser**
   - Aplikasi akan otomatis terbuka di `http://localhost:8501`
   - Jika tidak terbuka otomatis, buka browser dan akses URL tersebut

## 📊 Parameter Input

Aplikasi memerlukan 5 parameter utama untuk analisis:

### 🔵 Parameter Ukuran
- **Mean Radius (μm)**: Rata-rata jari-jari sel dalam mikrometer
- **Mean Area (μm²)**: Rata-rata luas area sel dalam mikrometer persegi

### 🟡 Parameter Bentuk
- **Mean Texture**: Rata-rata variasi intensitas skala abu-abu
- **Mean Smoothness**: Rata-rata kehalusan permukaan sel (0-1)

### 🟢 Parameter Perimeter
- **Mean Perimeter (μm)**: Rata-rata keliling sel dalam mikrometer

## 🔬 Teknologi yang Digunakan

- **Frontend**: Streamlit
- **Machine Learning**: Scikit-learn
- **Model**: Support Vector Machine (SVM)
- **Data Processing**: NumPy
- **Model Persistence**: Joblib

## 📁 Struktur File

```
breast_cancer_app/
├── app.py              # Aplikasi utama Streamlit
├── svm_model.pkl       # Model SVM yang telah dilatih
├── dt_model.pkl        # Model Decision Tree (opsional)
├── logo.png            # Logo aplikasi
├── requirements.txt    # Dependencies Python
└── README.md          # Dokumentasi ini
```

## ⚠️ Penting untuk Diperhatikan

### ⚕️ Disclaimer Medis

- **Alat Bantu Diagnostik**: Hasil ini hanya sebagai alat bantu analisis dan bukan diagnosis medis resmi
- **Konsultasi Medis Wajib**: Selalu konsultasikan hasil dengan dokter spesialis onkologi
- **Pemeriksaan Lanjutan**: Diperlukan tes laboratorium, biopsi, dan pemeriksaan medis lainnya
- **Tidak Menggantikan Skrining**: Tool ini tidak menggantikan mammografi, USG, atau pemeriksaan rutin

### 🔒 Keamanan Data

- Data yang dimasukkan tidak disimpan secara permanen
- Semua analisis dilakukan secara lokal
- Tidak ada data yang dikirim ke server eksternal

## 🛠️ Troubleshooting

### Model tidak ditemukan
```
❌ Model file tidak ditemukan. Pastikan file 'svm_model.pkl' ada di direktori yang sama.
```
**Solusi**: Pastikan file `svm_model.pkl` berada di direktori yang sama dengan `app.py`

### Error saat instalasi dependencies
**Solusi**: Gunakan virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Port sudah digunakan
**Solusi**: Gunakan port alternatif
```bash
streamlit run app.py --server.port 8502
```

## 📈 Performa Model

- **Dataset**: Wisconsin Diagnostic Breast Cancer (WDBCD)
- **Fitur**: Menganalisis 30+ parameter morfologis sel
- **Validasi**: Model telah divalidasi menggunakan teknik cross-validation
- **Akurasi**: Tingkat akurasi tinggi dalam deteksi kanker payudara

## 🤝 Kontribusi

Kontribusi untuk pengembangan aplikasi ini sangat diterima! Silakan:

1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📞 Support

Jika Anda mengalami masalah atau memiliki pertanyaan:

- 📧 Email: [gunturhanabi222@gmail.com.com]
- 💬 Issues: Gunakan GitHub Issues
- 📖 Dokumentasi: Lihat bagian FAQ di aplikasi

## 📄 Lisensi

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments

- Dataset: Wisconsin Diagnostic Breast Cancer (WDBCD)
- Scikit-learn team untuk library Machine Learning
- Streamlit team untuk framework web yang luar biasa
- Komunitas Python untuk dukungan dan kontribusi

---

**⚕️ Selalu konsultasikan dengan tenaga medis profesional untuk diagnosis yang akurat**

*Breast Cancer Prediction System v2.0 - Dikembangkan untuk membantu deteksi dini kanker payudara*
