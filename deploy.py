import streamlit as st
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load model
model = keras.models.load_model("CNN_eeg_model.h5")
model.compile(loss='binary_crossentropy', optimizer='adam',metrics=['acc',tf.keras.metrics.Recall(),tf.keras.metrics.AUC(),tf.keras.metrics.Precision()])

st.sidebar.subheader('About the App')
st.sidebar.write('EEG Classification App with Streamlit using a trained CNN model')
st.sidebar.write('This app will classify EEG signal and determine whether the subject is a Good counter or Bad counter (for whom the mental task required excessive efforts).')

#start the user interface
st.title("EEG Classification App")
st.write("Upload csv file containing EEG signal with 19 channel [Fp1, Fp2, F3, F4, F7, F8, T3,T4, C3, C4, T5, T6, P3, P4, O1, O2, Fz, Cz, Pz]")
st.write("Input example [s00.csv](https://drive.google.com/file/d/1wrWdREzw4z6rSK0kO3zkcYuHqjCz21Tp/view?usp=sharing)")

uploaded_file = st.file_uploader("Upload file with format .csv", type="csv")

if uploaded_file is not None:
    # read csv
    signal = pd.read_csv(uploaded_file, header=None)
    signal = signal.transpose().to_numpy()
    signal = signal.reshape(760,775)

    channel_index = st.selectbox("Select Channel", options=[i+1 for i in range(signal.shape[0])])
    
    # visualize signal
    plt.plot(signal[channel_index-1])

    plt.title(f'EEG Signal - Channel {channel_index}')
    plt.xlabel('Time')
    plt.ylabel('EEG Signal Amplitude')
    st.pyplot(plt.gcf())

if st.button('Classify', key='classify_button'):
    if uploaded_file is not None:      
        x_test = np.array([[signal]])

        predict = model.predict(x_test)

        if predict[0] > 0:
        # the predicted class is 1
            st.write(f"The subject is a Good Counter")
        else:
        # otherwise the predicted class is 0
            st.write(f"The subject is a Bad Counter")
    else:
        st.warning("you need to upload a csv file.")
