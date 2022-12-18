import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("lightgbm")

import streamlit as st
import pandas as pd
import pickle
from PIL import Image
from lightgbm import LGBMClassifier


st.write("""
# Patient Survival Prediction

This app predicts if your patient is healthy or in danger by means of patient's blood test.

""")


st.sidebar.header('Patient Health Information Form')

st.sidebar.markdown("""
[Example CSV file](https://github.com/meric2/Patient-Survival-Prediction-YAP470/blob/main/example.csv)
""")

uploaded_file = st.sidebar.file_uploader("Upload the patient's health report in a CSV file in the format of the example above.", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    s = df.columns[0]
    col = [str(s[0:3]),str(s[4:28]),str(s[29:58]),str(s[59:70]),str(s[71:83])]
    col = pd.Series(col)
    v = df.iloc[0][0]
    val = [[int(v[0:2]),float(v[3:7]),float(v[8:12]),int(v[13:15]),int(v[16:18])]]
    df = pd.DataFrame(data=val, columns=col)
else:
    def user_input_features():
        age = st.sidebar.slider('Age', 0, 100, 1)
        apache_4a_icu_death_prob = st.sidebar.slider('The APACHE IVa score of in ICU mortality', -1.0, 0.99, 0.01)
        apache_4a_hospital_death_prob = st.sidebar.slider('The APACHE IVa score of in-hospital mortality', -1.0, 0.99, 0.01)
        d1_spo2_min = st.sidebar.slider('The lowest peripheral oxygen saturation during the first 24 hours', 0, 100, 1)
        d1_sysbp_min = st.sidebar.slider('The lowest systolic blood pressure during the first 24 hours', 41, 160, 1)
        data = {'Age': age,
                'ICU APACHE IVa score': apache_4a_icu_death_prob,
                'In-hospital APACHE IVa score': apache_4a_hospital_death_prob,
                'Peripheral oxygen saturation': d1_spo2_min,
                'Systolic blood pressure': d1_sysbp_min}
        features = pd.DataFrame(data, index=[0])
        return features

    df = user_input_features()

st.subheader('Patient Health Information')
st.write(df)

model = pickle.load(open("model.pkl", 'rb'))
prediction = model.predict(df)

st.subheader('Prediction Result:')
if prediction == 0:
    st.write("**Survival**")
    st.write("The patient is healthy!")
if prediction == 1:
    st.write("**Mortality**")
    st.write("It is suggested that the patient stays under supervision.")

image = Image.open('photo.jpg')
st.image(image)
