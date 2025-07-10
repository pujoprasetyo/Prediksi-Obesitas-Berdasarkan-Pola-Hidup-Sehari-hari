# Analisis Hasil Prediksi Level Obesitas Berdasarkan Algoritma Baselearner, Bagging, dan Bosting

## I. Repository Outline
1. README.md - Penjelasan gambaran umum project
2. Model Building.ipynb - Main Notebook yang digunakan untuk pengolahan data dan pemodelan machine learning
3. Model Inference.ipynb - Notebook yang digunakan untuk proses inference / uji model terhadap data baru
4. list_cat_cols.txt - Teks berisi nama-nama kolom kategorikal
5. list_num_cols.txt - Teks berisi nama-nama kolom numerikal
6. url.txt - Link dataset dan model inference
7. Screenshoot Program.png - Tampilan aplikasi model deployment
8. deployment/ - Folder yang berisi file untuk model deployement menggunakan HuggingFace
9. eda.py - Kode program untuk menampilkan hasil eksplorasi data 
10. model.pkl - Hasil model machine learning yang dibuat
11. prediction.py - Kode program untuk menampilkan halaman prediksi obesitas
12. streamlit_app.py - Kode program untuk halaman streamlit
13. requirement.txt - Spesifikasi Library yang dibutuhkan untuk membangun model

## II.  Problem Background
Obesitas adalah sebuah penyakit yang diakibatkan oleh kelebihan lemak dalam tubuh. Obesistas dapat dipengaruhi oleh banyak faktor diantaranya faktor genetic, factor hormonal dan gaya hidup seperti pola makan, jenis makanan, kuantitas mengkonsumsi makanan dan juga aktifitas fisik. Hampir 70% kejadian obesitas disebabkan oleh pengaruh gaya hidup dan lingkungan. Perilaku masyarakat yang semakin konsumtif berdampak pada transisi pola makan tinggi kalori, tinggi lemak dan tinggi garam, misalnya seperti junkfood, hamburger, sosis, mie instant, gorengan dan minuman bersoda. Hal tersebut menimbulkan permasalahan dalam tubuh seperti lonjakan gula darah, penumpukan lemak, dan kurangnya gizi seimbang.

Obesitas dapat meningkatkan risiko penyakit jantung, diabetes, hipertensi, stroke, kanker, dan masalah pencernaan seperti GERD atau batu empedu. Oleh sebab itu perlu dilakukan screening terhadap tingkat obesitas secara teratur untuk memantau pola hidup dan kadar lemak dalam tubuh agar tingkat obesitas menjadi lebih terkontrol.

## Project Output
Hasil dari project yang dibuat antara lain :
1. Model machine learning untuk mendiagnosa level obesitas yang dialami oleh seseorang menggunakan metode klasifikasi. 
2. Rekomendasi kepada user mengenai berat badan / tinggi badan ideal serta pola hidup yang sesuai untuk mengurangi level obesitas. 
3. Website yang dapat digunakan untuk menggunakan model yang telah dibuat
4. Insight mengenai potensi bisnis yang dapat dilakukan.

## Data
Dataset yang digunakan untuk project ini diambil dari UC Irvine Machine Learning Repository dengan judul “Estimation of Obesity Levels Based On Eating Habits and Physical Condition”. 
Dataset berisi data Obesitas Level berdasarkan pola makan dan kondisi fisik responden yang diambil dari populasi penduduk Colombia, Peru, dan Mexico pada tahun 2017.
Dataset terdiri dari 17 kolom dan 2111 baris data.

## Method
Pada project ini terdapat 5 algoritma machine learning yang digunakan untuk mendapatkan hasil terbaik yaitu:
1. Descission Tree
2. K-Nearest Neightbors
3. Support Vector Machine (SVM)
4. Random Forest
5. CatBoost

Metode analisis data yang digunakan pada project ini meliputi beberapa method antara lain:

Visualisasi data -> menggambarkan grafik penjualan agar mudah dianalisis
Statistik inferensial -> menguji asumsi yang timbul berdasarkan data yang ada

Metode Evaluasi yang digunakan untuk menilai performa model adalah:
1. Accuracy Score
2. ROC AUC Score

## Stacks
Proses pengolahan data dilakukan menggunakan aplikasi VSCode dengan bahasa pemrograman Python Terdapat beberapa library yang digunakan untuk mempermudah proses analisis data, yaitu:
1. Pandas -> memproses dataset
2. Scipy -> melakukan perhitungan statistik
3. Seaborn -> menggambarkan visualisasi data
4. Scikit-learn -> library machine learning
5. CatBoost - library model catboosting
6. Winsorizer -> proses normalisasi data
7. Pipeline -> meringkas proses pengolahan data
8. Pickle -> menyimpan model machine learning
9. HuggingFace -> deployment model 

## Reference

Dataset for estimation of obesity levels based on eating habits and physical condition in individuals from Colombia, Peru and Mexico (Palechor., 2019) [Link](https://www.sciencedirect.com/science/article/pii/S2352340919306985)

Skrining Obesitas dan Edukasi Dampak Obesitas pada Anak di SDN 49/IV Kota Jambi (Ekawati, dkk., 2020)[Link](https://garuda.kemdikbud.go.id/documents/detail/1944834) 

Aktivitas, Konsumsi Makanan, Faktor Fisiologis, dan Riwayat Obesitas Keluarga Kaitannya dengan Obesitas pada Pegawai (Okfiani, dkk., 2022)[Link](https://e-journal.unair.ac.id/AMNT/article/view/20060/22213) 

Dataset dapat diakses pada link berikut:
https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition 

Model Deployment dapat diakses pada link berikut:
https://huggingface.co/spaces/prasetyoaji/Milestone2

Gambar tampilan Hasil Web Deployemnt:

![Tampilan Program](./Screnshoot%20Program.PNG)
