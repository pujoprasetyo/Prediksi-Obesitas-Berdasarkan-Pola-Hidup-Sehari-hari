#Library
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image

def run():
  # Menambahkan Gambar
  image = Image.open('./src/bmi.jpg')
  st.image(image)

  # Title
  st.title('Halaman ini dibuat untuk menampilkan hasil Explatory Data Analysis (EDA) dari dataset \
  obesity level berdasarkan pola hidup masyarakat')
  st.markdown('-------')

  # Menampilkan df
  st.write('## Dataset yang digunakan dapat dilihat pada tabel berikut')
  df = pd.read_csv('./src/data.csv')
  st.dataframe(df)
  st.markdown('-------')

  # ------------ EDA 1 ------------
  st.write('## 1. Pengaruh makanan tinggi kalori terhadap level obesitas')

  # Ambil level obesitas unik
  obesity_levels = df['Obesity_Level'].unique()

  # Subplot grid (misal 4x4 agar cukup)
  fig, axs = plt.subplots(nrows=4, ncols=4, figsize=(20, 20))
  axs = axs.flatten()

  # Buat pie chart per level obesitas
  for i, level in enumerate(obesity_levels):
      subset = df[df['Obesity_Level'] == level]
      cal_counts = subset['Eating_High_Calories'].value_counts()

      axs[i].pie(cal_counts, labels=cal_counts.index, autopct='%1.1f%%', startangle=90)
      axs[i].set_title(f'Obesity: {level}', fontsize=14)
      axs[i].axis('equal')

  # Hapus subplot kosong jika jumlah level < 16
  for j in range(len(obesity_levels), len(axs)):
      fig.delaxes(axs[j])

  plt.tight_layout()

  # Tampilkan di Streamlit
  st.pyplot(fig)

  st.write('Berdasarkan visualisasi yang digambarkan menggunakan pieplot. Orang yang dengan berat badan normal atau kurang cenderung lebih sedikit yang mengkonsumsi makanan tinggi kalori. Sedangkan orang dengan obesitas level yang tinggi cenderung suka mengkonsumsi makanan tinggi kalori.')
  st.markdown('-------')

  # ------------ EDA 2 ------------
  st.write('## 2. Pengaruh Rokok dan Alkohol terhadap obesitas')
  # Buat canvas figure
  fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))

  #Contingency Table
  table_smoke_obesity = pd.crosstab(df['Obesity_Level'],df['SMOKE'])
  table_alcohol_obesity = pd.crosstab(df['Obesity_Level'],df['Alcohol_Freq'])

  # Heatmap 1: SMOKE vs Obesity_Level
  sns.heatmap(table_smoke_obesity, annot=True, cmap='crest', fmt='d', ax=axs[0])
  axs[0].set_title("SMOKE vs Obesity_Level")
  axs[0].set_xlabel("SMOKE")
  axs[0].set_ylabel("Obesity Level")

  # Heatmap 2: Alcohol_Freq vs Obesity_Level
  sns.heatmap(table_alcohol_obesity, annot=True, cmap='crest', fmt='d', ax=axs[1])
  axs[1].set_title("Alcohol_Freq vs Obesity_Level")
  axs[1].set_xlabel("Alcohol Frequency")
  axs[1].set_ylabel("")

  # Rapiin layout dan tampilkan di Streamlit
  plt.tight_layout()
  st.pyplot(fig)

  st.write('Dari visualisasi yang ditampilkan terdapat hubungan yang nyata antara rokok dan obesity level, namun hubungan tersebut negatif. Jika kita lihat orang yang jarang merokok lebih banyak yang mengalami obesitas dibandingkan orang yang merokok.')
  st.write('Sedangkan pada tabel hubungan antara alkohol dan obesitas level, orang yang sering mengkonsumsi alkohol dan jarang mengkonsumsi alkohol mengalami obesitas level yang bervariasi. Orang yang mengkonsumsi alkohol dengan frekuensi rendah-sedang cenderung lebih banyak yang terdeteksi memiliki obesitas.')
  st.markdown('-------')

  # ------------ EDA 3 ------------
  st.write('## 3. Hubungan antara physical activity dan obesitas')
  fig = plt.figure(figsize=(15,5))
  sns.scatterplot(data=df, x='Physical_Activity_Freq', y='Obesity_Level', palette='bright')
  st.pyplot(fig)
  st.write('Berdasarkan scatter plot diatas dapat dilihat bahwa semakin tinggi level obesitas seseorang maka semakin rendah physical activity yang dilakukan.')
  st.markdown('-------')

  # ------------ EDA 4 ------------
  st.write('## 4. Distribusi tinggi dan berat badan berdasarkan obesitas level')
  fig = plt.figure(figsize=(15,5))
  sns.scatterplot(data=df, x='Weight', y='Height', hue='Obesity_Level', palette='bright')
  plt.title('Distribusi Tinggi Badan dan Berat Badan')
  plt.tight_layout()
  plt.show()
  st.pyplot(fig)
  st.write('Dari visualisasi data yang ditampilkan poin yang dapat diambil yaitu:')
  st.write('1. Orang dengan berat badan yang kurang (ungu) cenderung memiliki berat badan dibawah 60kg dengan tinggi badan 1,5m - 1.9m')
  st.write('2. Orang dengan berat badan normal (biru) memiliki rentang berat badan yang bervariasi antara 40-80 kg, tinggi badan orang normal berkisar antara 1,5-1,9m. ')
  st.write('3. Orang dengan overweight level 1 (orange) memiliki rentang bb dari 50 - 90 kg dan tb 1,4-1,9m')
  st.write('4. Orang dengan overweight level 2 (hijau) memiliki rentang bb dari 60 - 100 kg dan tb 1,5-1,9m')
  st.write('5. Orang dengan obesity level 1 (merah)  memiliki rentang bb dari 80 - 120 kg dan tb 1,5-2m')
  st.write(' 6. Orang dengan obesity level 2 (coklat) memiliki rentang bb dari 100 - 130 kg dan tb 1,6-1,9m')
  st.write('7. Orang dengan obesity level 3 (pink) memiliki rentang bb dari 100 hingga 180 kg atau lebih dan tb 1,55-1,9m')
  st.write('Berdasarkan data tersebut dapat ditarik kesimpulan bahwa berat badan sangat berpengaruh terhadap obesity level, semakin tinggi nilai berat badan seseorang maka semakin tinggi obesitas level oran tersebut.')
  st.markdown('-------')


  # ------------ EDA 5 ------------
  st.write('## 5. Jumlah konsumsi air harian')
  fig = plt.figure(figsize=(15,5))
  sns.barplot(data=df, x='Daily_Water', y='Obesity_Level', palette='bright')
  st.pyplot(fig)
  st.write('Rata-rata konsumsi air harian dari seluruh data sekitar 1,5 hingga 2 liter perhari. Orang dengan kelebihan berat badan atau obesitas cenderung mengkonsumsi air lebih banyak dibandingkan orang dengan berat badan normal. Jumlah konsumsi air harian tertinggi dimiliki oleh kelas obesity tipe 3 dengan jumlah konsumsi air harian lebih dari 2 liter per hari.')
  st.markdown('-------')


  # ------------ EDA 6 ------------
  st.write('## 6. Distribusi tinggi dan berat badan berdasarkan obesitas level')
  fig = plt.figure(figsize=(15,5))
  sns.countplot(data=df, x='Eating_Vegi_Freq', hue='Obesity_Level')
  st.pyplot(fig)
  st.write('Berdasarkan visualisasi data yang ditampilkan, sebagian besar data sampel sering mengkonsumsi sayuran setiap harinya. Orang dengan obesitas malah lebih cenderung mengkonsumsi sayuran setiap kali mereka makan. Bahkan frekuensi konsumsi sayuran pada penderita obesity tipe 3 sangat besar dibandingkan data lainnya, hal tersebut kemungkinan terjadi karena mereka sering mengkonsumsi sayuran sebagai camilan atau snack setiap harinya.')
  st.markdown('-------')


  # ------------ EDA 7 ------------
  st.write('## 7. Mode Transportasi yang digunakan')
  fig = plt.figure(figsize=(15,5))
  sns.countplot(data=df, x='MTRANS', hue='Obesity_Level', width=0.6)
  st.pyplot(fig)
  st.write('Public transportation merupakan moda transportasi yang paling banyak digunakan oleh seluruh orang, disusul dengan mobil dan berjalan kaki. Transportasi dengan motor dan sepeda merupakan moda transportasi yang paling sedikit digunakan.')
  st.write('Jika dilihat berdasarkan obesity level orang dengan obesitas paling banyak menggunakan moda transportasi publik. Hampir seluruh orang dengan obesitas tipe 3 memilih transportasi publik sebagai moda transportasi sehari-hari.')
  st.write('Kemudian pada moda transportasi dengan jalan kaki, orang berat badan normal jauh lebih banyak yang berpergian dengan jalan kaki dibandingkan orang dengan obesitas.')
  st.write('Pada moda transportasi mobil, orang dengan obesitas lebih banyak yang menggunakan kendaraan mobil jika dibandingkan orang dengan berat badan normal atau kurang.')
  st.write('Dari seluruh hasil analisis data berdasarkan moda transportasi yang digunakan, dapat disimpulkan bahwa orang dengan obesitas lebih cenderung menggunakan kendaraan untuk berpergian dan menghindari jalan kaki')

  

if __name__ == '__main__':
  run()