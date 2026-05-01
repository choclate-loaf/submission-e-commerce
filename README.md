# 📊 Proyek Analisis Data E-Commerce

## 👤 Informasi
- **Nama:** [Shinta Khumaira]  
- **Email:** [Banoffe1993@gmail.com]  
- **ID Dicoding:** [CDCC942D6X1050]  

---

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data e-commerce guna memahami tren penjualan serta perilaku pelanggan. Analisis dilakukan menggunakan Exploratory Data Analysis (EDA) dan dilengkapi dengan visualisasi data serta dashboard interaktif menggunakan Streamlit.

---

## 🎯 Pertanyaan Bisnis
1. Bagaimana tren jumlah order dan total revenue bulanan selama periode tertentu serta kapan terjadi puncak penjualan tertinggi?
2. Bagaimana segmentasi pelanggan berdasarkan RFM (Recency, Frequency, Monetary) dan bagaimana kontribusi masing-masing segmen terhadap revenue?

---

## 🛠️ Teknologi yang Digunakan
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit

---

## 📂 Struktur Proyek
submission/
│
├── dashboard/
│   ├── dashboard.py
│   └── data/
│       ├── orders_dataset.csv
│       ├── order_payments_dataset.csv
│       └── customers_dataset.csv
│
├── notebook.ipynb
├── requirements.txt
└── README.md

---

## ▶️ Cara Menjalankan Dashboard (Lokal)

1. Install dependencies:
pip install -r requirements.txt

2. Jalankan Streamlit:
streamlit run dashboard/dashboard.py

3. Buka browser:
http://localhost:8501

---

## ☁️ Deploy ke Streamlit Cloud
1. Upload project ke GitHub
2. Buka Streamlit Cloud
3. Klik **New App**
4. Pilih repository
5. Masukkan path:
dashboard/dashboard.py
6. Klik Deploy

---

## 📊 Insight Utama
- Terjadi peningkatan signifikan pada jumlah order dan revenue pada awal tahun 2017
- Sebagian besar pelanggan hanya melakukan satu kali transaksi
- Pelanggan dengan nilai transaksi tinggi memberikan kontribusi besar terhadap revenue
- Diperlukan strategi untuk meningkatkan retensi pelanggan

---

## 🚀 Rekomendasi
- Meningkatkan strategi retensi pelanggan melalui program loyalitas
- Memberikan promosi khusus untuk pelanggan bernilai tinggi
- Melakukan re-engagement kepada pelanggan yang tidak aktif

---

## 🔗 Dashboard Online
(Tambahkan link Streamlit Cloud di sini setelah deploy)

---

## 📎 Catatan
Pastikan semua file dataset tersedia di dalam folder `dashboard/data/` agar dashboard dapat berjalan dengan baik.
