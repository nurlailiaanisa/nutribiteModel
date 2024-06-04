# Rekomendasi Resep Berdasarkan KNN dan TF-IDF

Proyek ini menggunakan teknik *Natural Language Processing* (NLP) dan *Machine Learning* untuk merekomendasikan resep makanan yang mirip dengan resep yang disukai pengguna. Model K-Nearest Neighbors (KNN) dan TF-IDF digunakan untuk menemukan resep yang paling relevan.

## Daftar Isi
- [Pendahuluan](#pendahuluan)
- [Fitur](#fitur)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Lisensi](#lisensi)

## Pendahuluan

Proyek ini bertujuan untuk memberikan rekomendasi resep makanan kepada pengguna berdasarkan resep yang mereka sukai. Dengan memanfaatkan TF-IDF untuk mengubah teks resep menjadi vektor dan model KNN untuk mencari kemiripan antar resep, proyek ini dapat menemukan resep yang mirip dan sesuai dengan preferensi pengguna.

## Fitur

- Memuat dan memproses dataset resep makanan.
- Mengubah teks resep menjadi representasi vektor menggunakan TF-IDF.
- Melatih model KNN untuk mencari resep yang mirip.
- Memberikan rekomendasi resep berdasarkan input pengguna.

## Instalasi

Ikuti langkah-langkah berikut untuk menginstal dan menjalankan proyek ini di lingkungan lokal Anda:

1. **Clone repositori ini:**

   ```bash
   git clone https://github.com/nurlailiaanisa/nutribiteModel.git
   cd nutribiteModel

2. **Instalasi Libery:**
   ```bash
   pip install pandas scikit-learn

3. **Buat environment virtual dan aktifkan::**
   ```bash
   python -m venv env
   source env/bin/activate   # Untuk pengguna Unix/macOS
   .\env\Scripts\activate    # Untuk pengguna Windows

## Penggunaan

 1. **Latih model dan simpan:**
    ```bash
    python mode.py

2. **Uji model dan dapatkan rekomendasi:**
   ```bash
   python test_model.py

## Lisensi
- IMT
