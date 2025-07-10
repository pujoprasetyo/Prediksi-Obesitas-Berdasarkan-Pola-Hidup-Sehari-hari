# Import library
import streamlit as st
import pickle
import pandas as pd
from PIL import Image

# Load model
model = pickle.load(open('./src/model.pkl', 'rb'))

def run():
    # Title
    st.title('Aplikasi Prediksi Level Obesitas')

    # Sub Header
    st.subheader('Page ini berisi aplikasi untuk memprediksi level obesitas berdasarkan pola hidup sehari-hari')

    # Menambahkan Gambar
    image = Image.open('./src/image1.png')
    st.image(image)

    # Membuat header form
    st.markdown("<h3 style='text-align:center;'>Silahkan Isi Form Dibawah untuk Melakukan Prediksi</h3>", unsafe_allow_html=True)

    # Membuat form
    with st.form(key='fifa-2022'):

        # Membuat option value agar value sebenarnya dengan tampilan website berbeda
        opsi1 = {
            "Laki-laki": "Male",
            "Perempuan": "Female"
        }
        
        opsi2 = {
            "Iya": "yes",
            "Tidak": "no"
        }

        opsi3 = {
            "Kadang-kadang": "Sometimes",
            "Sering": "Always",
            "Tidak Pernah": "Never",
        }

        opsi4 = {
            "Tidak": "no",
            "Jarang": "Frequenly",
            "Kadang-kadang": "Sometimes",
            "Sering": "Always"
        }

        opsi5 = {
            "Berjalan kaki": "Walking",
            "Bersepeda": "Bike",
            "Sepeda motor": "Motorbike",
            "Mobil": "Automobile",
            "Transportasi Umum": "Public_Transportation"
        }       

        name = st.text_input('Nama', value='--nama anda--', help='Masukkan nama anda')
        gender = st.selectbox('Jenis Kelamin :', list(opsi1.keys()), index=0, help='Masukkan jenis kelamin')
        gender_value = opsi1[gender]
        age = st.number_input('Umur :', min_value=0, max_value=100, step=1, help='Masukkan umur anda')
        weight = st.number_input('Berat Badan :', min_value=0, max_value=200, step=1, help='Masukkan berat badan anda')
        height = st.number_input('Tinggi Badan : ', min_value=0,
                            max_value=300, step=1, help='Masukkan Tinggi Badan Anda')
        
        st.markdown('----')

        #Form Lanjutan
        gen = st.radio('Apakah anda memiliki riwayat keluarga yang terkena obesitas: ', list(opsi2.keys()), index=0)
        gen_value = opsi2[gen]
        calory_eating = st.radio('Apakah anda sering mengkonsumsi makanan tinggi kalori : ', list(opsi3.keys()), index=0)
        calory_value = opsi3[calory_eating]
        vegi = st.radio('Apakah anda sering mengkonsumsi sayuran : ', list(opsi3.keys()), index=0)
        vegi_value = opsi3[vegi]
        daily_meals = st.number_input('Berapa kali anda makan setiap hari :', min_value=0, max_value=10, step=1)
        snack = st.radio('Apakah anda suka mengkonsumsi makanan ringan : ', list(opsi4.keys()), index=0)
        snack_value = opsi4[snack]
        smoke = st.radio('Apakah anda perokok : ', list(opsi2.keys()), index=0)
        smoke_value = opsi2[smoke]
        daily_water = st.number_input('Berapa liter konsumsi air harian anda :', min_value=0, max_value=10, step=1)
        monitoring = st.radio('Apakah anda menghitung jumlah kalori harian anda : ', list(opsi2.keys()), index=0)
        monitor_value = opsi2[monitoring]
        physical = st.number_input('Seberap sering anda melakukan aktifitas fisik (olahraga) setiap minggu :', min_value=0, max_value=10, step=1)
        alcohol = st.radio('Apakah anda mengkonsumsi alkohol : ', list(opsi4.keys()), index=0)
        alcohol_value = opsi4[alcohol]
        trans = st.radio('Jenis transportasi apa yang anda gunakan untuk berpergian : ', list(opsi5.keys()), index=0)
        trans_value = opsi5[trans]

        
        submitted = st.form_submit_button('Predict')

        # Inference Data
        data_inf = {
                'Gender': gender_value,
                'Age': age,
                'Height': height,
                'Weight': weight,
                'genetic_overweight': gen_value,
                'Eating_High_Calories': calory_value,
                'Eating_Vegi_Freq': vegi_value,
                'Daily_Meals': daily_meals,
                'Eating_Snack_Freq': snack_value,
                'SMOKE': smoke_value,
                'Daily_Water': daily_water,
                'Calories_Monitoring': monitor_value,
                'Physical_Activity_Freq': physical,
                'Alcohol_Freq': alcohol_value,
                'MTRANS': trans_value
        }

        data_inf= pd.DataFrame([data_inf])

        # Membuat summary data yang akan ditampilkan agar tidak membingungkan user karena nama kolom yang berbeda
        data_display = {
                'Jenis Kelamin': gender,
                'Umur': age,
                'Tinggi Badan': height,
                'Berat Badan': weight,
                'Riwayat Obesitas': gen,
                'Makanan Berkalori': calory_eating,
                'Konsumsi Sayuran': vegi,
                'Jumlah Makan Sehari': daily_meals,
                'Snack': snack,
                'Rokok': smoke,
                'Jumlah Air Harian': daily_water,
                'Monitor Jumlah Kalori': monitoring,
                'Olahraga': physical,
                'Alcohol': alcohol,
                'Transportasi': trans
        }
        data_display = pd.DataFrame([data_display])
       
        # Membuat Kategori
        kategori0= ['Insufficient_Weight']
        kategori1= ['Normal_Weight']
        kategori2= ['Overweight_Level_I','Overweight_Level_II']
        kategori3= ['Obesity_Type_I','Obesity_Type_II', 'Obesity_Type_II']

        if submitted:
            data_display
            # Model
            y_pred_inf = model.predict(data_inf)

            if y_pred_inf in kategori0:
                st.write('### Prediksi Level Obesitas :')
                st.warning(f"### {y_pred_inf} (Berat badan kurang)")
                st.markdown('----')
                st.write('#### Rekomendasi :')
                st.write('1. Tingkatkan jumlah kalori harian')
                st.write('2. Kurangi aktivitas dengan intensitas berat')

            elif y_pred_inf in kategori1:
                st.write('### Prediksi Level Obesitas :')
                st.success(f"### {y_pred_inf} (Berat badan ideal)")
                st.markdown('----')
                st.write('#### Rekomendasi :')
                st.write('1. Jaga jumlah kalori harian untuk menghindari obesitas')
                st.write('2. Tingkatkan aktivitas fisik untuk meningkatkan massa otot')

            elif y_pred_inf in kategori2:
                st.write('### Prediksi Level Obesitas :')
                st.warning(f"### {y_pred_inf} (Mulai kelebihan berat badan)")
                st.markdown('----')
                st.write('#### Rekomendasi :')
                st.write('1. Kurangi konsumsi makanan tinggi kalori')
                st.write('2. Hindari pola hidup kurang sehat seperti merokok / alkohol')
                st.write('3. Tingkatkan aktivitas fisik untuk mengurangi lemak ditubuh')

            elif y_pred_inf in kategori3:
                st.write('### Prediksi Level Obesitas :')
                st.error(f"### {y_pred_inf} (Obesitas serius)")
                st.markdown('----')
                st.write('#### Rekomendasi :')
                st.write('1. Tingkatkan konsumsi air harian')
                st.write('2. Kurangi konsumsi makanan tinggi kalori')
                st.write('3. Hindari pola hidup kurang sehat seperti merokok / alkohol')
                st.write('4. Lakukan diet untuk mengurangi jumlah kalori harian')
                st.write('5. Tingkatkan aktivitas fisik untuk mengurangi lemak ditubuh')

if __name__ == '__main__':
  run()