# CNN-EEG-Classification

### Description

EEG Classification App with Streamlit using a trained CNN model

This app will classify EEG signal and determine whether the subject is a Good counter or Bad counter (for whom the mental task required excessive efforts).

### Contributor

- I Made Alit Darma Putra	(2008561045)
- I Nengah Oka Darmayasa 	(2008561070)
- I Made Teja Sarmandana	(2008561098)

### Dataset

This dataset consists of 36 files in .csv format which are the results of recording 36 different subjects. In each file, there are 19 data columns which are the recording channels used, including Fp1, Fp2, F3, F4, F7, F8, T3, T4, C3, C4, T5, T6, P3, P4, O1, O2, Fz, Cz, and Pz. There are 2 class labels used in this dataset, namely a good counter (Good Counter) or a bad counter (Bad Counter).

https://www.kaggle.com/code/amananandrai/36-subject-eeg-data-on-cnn-with-smote/input

### Tech Stack

- Python
- Streamlit

### How to run?

1. Install library

   ```
   pip install -r requirements. txt
   ```
3. Run the app
   
   ```
   streamlit run ./deploy.py
   ```

### CNN Architecture

![image](https://github.com/alitdarmaputra/CNN-EEG-Classification/assets/74844470/efb55af2-8490-418d-b94f-7e5e2f03fe54)

<img width="370" alt="image" src="https://github.com/alitdarmaputra/CNN-EEG-Classification/assets/74844470/04c908a9-8772-4875-af3b-220a30986bf5">

### App Preview

![image](https://github.com/alitdarmaputra/CNN-EEG-Classification/assets/74844470/2d83c243-c012-4083-8c22-a91982c62c15)

![image](https://github.com/alitdarmaputra/CNN-EEG-Classification/assets/74844470/6165af02-b14f-48ab-8465-1736e4fb8a00)

![image](https://github.com/alitdarmaputra/CNN-EEG-Classification/assets/74844470/9e8cd934-9009-4106-9bb7-8816449834f3)

