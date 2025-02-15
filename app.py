import streamlit as st
import pickle 

with open('C:\\Users\\deeshika & Sherya\\OneDrive\\Desktop\\New folder (2)\\trained_model.sav', 'rb') as file:
    model = pickle.load(file)
st.title("Welcome to thyroid cancer prediction")
age=int(st.number_input("Enter age",step=1))
gender = st.selectbox(
    "Select gender",
    ("Male", "Female")
)
country = st.selectbox(
    "Select country",
    ('Russia', 'Germany', 'Nigeria', 'India', 'UK', 'South Korea',
       'Brazil', 'China', 'Japan', 'USA')
)
ethnicity = st.selectbox(
    "Select ethnicity",
    ('Caucasian', 'Hispanic', 'Asian', 'African', 'Middle Eastern')
)

selected_options = st.multiselect(
    'Select conditions true for you',
    ['Family_History','Radiation_Exposure','Iodine_Deficiency','Smoking','Obesity','Diabetes']
)
tsh=float(st.number_input("Enter tsh"))
t3=float(st.number_input("Enter t3"))
t4=float(st.number_input("Enter t4"))
nodule=float(st.number_input("Enter nodule size"))
risk=st.selectbox(
    "Select risk",('Low', 'Medium', 'High'))
if st.button('Predict!'):
    list=[]
    list.append(age)
    if gender=='Male':
        list.append(1)
    else:
        list.append(0)
    
    cv=[6, 2, 5, 3, 8, 7, 0, 1, 4, 9]
    ck=['Russia', 'Germany', 'Nigeria', 'India', 'UK', 'South Korea','Brazil', 'China', 'Japan', 'USA']
    c=dict(zip(ck, cv))
    list.append(c[country])
    ev=[2, 3, 1, 0, 4]
    ek=['Caucasian', 'Hispanic', 'Asian', 'African', 'Middle Eastern']
    e=dict(zip(ek,ev))
    list.append(e[ethnicity])
   
    if 'Family_History' in selected_options:
        list.append(1)
    else:
        list.append(0)
    if 'Radiation_Exposure' in selected_options:
        list.append(1)
    else:
        list.append(0)
    if 'Iodine_Deficiency' in selected_options:
        list.append(1)
    else:
        list.append(0)
    if 'Smoking' in selected_options:
        list.append(1)
    else:
        list.append(0)
    if 'Obesity' in selected_options:
        list.append(1)
    else:
        list.append(0)
    if 'Diabetes' in selected_options:
        list.append(1)
    else:
        list.append(0)

    list.append(tsh)
    list.append(t3)
    list.append(t4)
    list.append(nodule)
    rk=['Low', 'Medium', 'High']
    rv=[1, 2, 0]
    r=dict(zip(rk, rv))

    list.append(r[risk])
    predicted=model.predict([list])
    if predicted==1:
        st.write("Tumour is cancerous/malignant")
    else:
        st.write("Tumour is benign")
    
    
