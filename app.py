import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Change Name & Logo
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")

# Hiding Streamlit add-ons
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Adding Background Image
background_image_url = "https://www.intertek.com/siteassets/blogs/2024-04-16-blog-widebanner.jpg"  # Replace with your image URL

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url({background_image_url});
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stAppViewContainer"]::before {{
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(0, 0, 0, 0.7);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load the saved models
models = {
    'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
}

# Create a dropdown menu for disease prediction
selected = st.selectbox(
    'Select a Disease to Predict',
    ['Heart Disease Prediction',
     'Parkinsons Prediction',
     'Lung Cancer Prediction',
     'Thyroid Disease Prediction']
)

def display_input(label, tooltip, key, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease')
    st.write("Enter the following details to predict heart disease:")

    age = display_input('Age', 'Enter age of the person', 'age', 'number')
    sex = display_input('Sex (1 = male; 0 = female)', 'Enter sex of the person', 'sex', 'number')
    cp = display_input('Chest Pain types (0, 1, 2, 3)', 'Enter chest pain type', 'cp', 'number')
    trestbps = display_input('Resting Blood Pressure', 'Enter resting blood pressure', 'trestbps', 'number')
    chol = display_input('Serum Cholesterol in mg/dl', 'Enter serum cholesterol', 'chol', 'number')
    fbs = display_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', 'Enter fasting blood sugar', 'fbs', 'number')
    restecg = display_input('Resting Electrocardiographic results (0, 1, 2)', 'Enter resting ECG results', 'restecg', 'number')
    thalach = display_input('Maximum Heart Rate achieved', 'Enter maximum heart rate', 'thalach', 'number')
    exang = display_input('Exercise Induced Angina (1 = yes; 0 = no)', 'Enter exercise induced angina', 'exang', 'number')
    oldpeak = display_input('ST depression induced by exercise', 'Enter ST depression value', 'oldpeak', 'number')
    slope = display_input('Slope of the peak exercise ST segment (0, 1, 2)', 'Enter slope value', 'slope', 'number')
    ca = display_input('Major vessels colored by fluoroscopy (0-3)', 'Enter number of major vessels', 'ca', 'number')
    thal = display_input('Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)', 'Enter thal value', 'thal', 'number')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        heart_prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
        st.success(heart_diagnosis)

# Lung Cancer Prediction Page
if selected == "Lung Cancer Prediction":
    st.title("Lung Cancer")
    st.write("Enter the following details to predict lung cancer:")

    GENDER = display_input('Gender (1 = Male; 0 = Female)', 'Enter gender of the person', 'GENDER', 'number')
    AGE = display_input('Age', 'Enter age of the person', 'AGE', 'number')
    SMOKING = display_input('Smoking (1 = Yes; 2 = No)', 'Enter if the person smokes', 'SMOKING', 'number')
    YELLOW_FINGERS = display_input('Yellow Fingers (1 = Yes; 2 = No)', 'Enter if the person has yellow fingers', 'YELLOW_FINGERS', 'number')
    ANXIETY = display_input('Anxiety (1 = Yes; 2 = No)', 'Enter if the person has anxiety', 'ANXIETY', 'number')
    PEER_PRESSURE = display_input('Peer Pressure (1 = Yes; 2 = No)', 'Enter if the person is under peer pressure', 'PEER_PRESSURE', 'number')
    CHRONIC_DISEASE = display_input('Chronic Disease (1 = Yes; 2 = No)', 'Enter if the person has a chronic disease', 'CHRONIC_DISEASE', 'number')
    FATIGUE = display_input('Fatigue (1 = Yes; 2 = No)', 'Enter if the person experiences fatigue', 'FATIGUE', 'number')
    ALLERGY = display_input('Allergy (1 = Yes; 2 = No)', 'Enter if the person has allergies', 'ALLERGY', 'number')
    WHEEZING = display_input('Wheezing (1 = Yes; 2 = No)', 'Enter if the person experiences wheezing', 'WHEEZING', 'number')
    ALCOHOL_CONSUMING = display_input('Alcohol Consuming (1 = Yes; 2 = No)', 'Enter if the person consumes alcohol', 'ALCOHOL_CONSUMING', 'number')
    COUGHING = display_input('Coughing (1 = Yes; 2 = No)', 'Enter if the person experiences coughing', 'COUGHING', 'number')
    SHORTNESS_OF_BREATH = display_input('Shortness Of Breath (1 = Yes; 2 = No)', 'Enter if the person experiences shortness of breath', 'SHORTNESS_OF_BREATH', 'number')
    SWALLOWING_DIFFICULTY = display_input('Swallowing Difficulty (1 = Yes; 2 = No)', 'Enter if the person has difficulty swallowing', 'SWALLOWING_DIFFICULTY', 'number')
    CHEST_PAIN = display_input('Chest Pain (1 = Yes; 2 = No)', 'Enter if the person experiences chest pain', 'CHEST_PAIN', 'number')

    lungs_diagnosis = ''
    if st.button("Lung Cancer Test Result"):
        lungs_prediction = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        lungs_diagnosis = "The person has lung cancer disease" if lungs_prediction[0] == 1 else "The person does not have lung cancer disease"
        st.success(lungs_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease")
    st.write("Enter the following details to predict Parkinson's disease:")

    fo = st.number_input('MDVP:Fo(Hz)', step=0.00001, format="%.5f")
    fhi = st.number_input('MDVP:Fhi(Hz)', step=0.00001, format="%.5f")
    flo = st.number_input('MDVP:Flo(Hz)', step=0.00001, format="%.5f")
    Jitter_percent = st.number_input('MDVP:Jitter(%)', step=0.00001, format="%.5f")
    Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', step=0.00001, format="%.5f")
    RAP = st.number_input('MDVP:RAP', step=0.00001, format="%.5f")
    PPQ = st.number_input('MDVP:PPQ', step=0.00001, format="%.5f")
    DDP = st.number_input('Jitter:DDP', step=0.00001, format="%.5f")
    Shimmer = st.number_input('MDVP:Shimmer', step=0.00001, format="%.5f")
    Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', step=0.00001, format="%.5f")
    APQ3 = st.number_input('Shimmer:APQ3', step=0.00001, format="%.5f")
    APQ5 = st.number_input('Shimmer:APQ5', step=0.00001, format="%.5f")
    APQ = st.number_input('MDVP:APQ', step=0.00001, format="%.5f")
    DDA = st.number_input('Shimmer:DDA', step=0.00001, format="%.5f")
    NHR = st.number_input('NHR', step=0.00001, format="%.5f")
    HNR = st.number_input('HNR', step=0.00001, format="%.5f")
    RPDE = st.number_input('RPDE', step=0.00001, format="%.5f")
    DFA = st.number_input('DFA', step=0.00001, format="%.5f")
    spread1 = st.number_input('Spread1', step=0.00001, format="%.5f")
    spread2 = st.number_input('Spread2', step=0.00001, format="%.5f")
    D2 = st.number_input('D2', step=0.00001, format="%.5f")
    PPE = st.number_input('PPE', step=0.00001, format="%.5f")

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        input_data = [[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, 
                       APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]]
        
        parkinsons_prediction = models['parkinsons'].predict(input_data)
        parkinsons_diagnosis = "✅ The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "❎ The person does not have Parkinson's disease"
        st.success(parkinsons_diagnosis)
                
# Hypo-Thyroid Prediction Page
if selected == "Thyroid Disease Prediction":
    st.title("Thyroid Disease Prediction")
    st.write("Enter the following details to predict thyroid disease:")

    age = display_input('Age', 'Enter age of the person', 'age', 'number')
    sex = display_input('Sex (1 = Male; 0 = Female)', 'Enter sex of the person', 'sex', 'number')
    on_thyroxine = display_input('On Thyroxine (1 = Yes; 0 = No)', 'Enter if the person is on thyroxine', 'on_thyroxine', 'number')
    tsh = st.number_input('TSH Level (e.g. 6.6)', min_value=0.0, step=0.1, format="%.2f")
    t3_measured = st.number_input('T3 Measured (1 = Yes; 0 = No)', min_value=0.0, max_value=1.0, step=1.0, format="%.0f")
    t3 = st.number_input('T3 Level (e.g. 1.4)', min_value=0.0, step=0.1, format="%.2f")
    tt4 = st.number_input('TT4 Level (e.g. 99)', min_value=0.0, step=0.1, format="%.2f")

    thyroid_diagnosis = ''
    if st.button("Thyroid Test Result"):
        input_data = [[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]]
        thyroid_prediction = models['thyroid'].predict(input_data)
        thyroid_diagnosis = "The person has Thyroid disease" if thyroid_prediction[0] == 1 else "The person does not have Thyroid disease"
        st.success(thyroid_diagnosis)
        
# Footer
st.sidebar.markdown('---')
st.sidebar.markdown('Made with ❤️ by [Rishabh Mehta](https://www.linkedin.com/in/rishabhmehta2003) | [GitHub](https://github.com/DoRishabh)')
