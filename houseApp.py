import pandas as pd
import pickle as pk
import streamlit as st

#model=pk.load(open('D:\housePrediction\House_prediction_model.pkl','rb'))
# Open the file in binary read mode
with open('D:\housePredictionProject\House_prediction_model.pkl', 'rb') as file:
    model = pk.load(file)


st.header('House Prices Predictor')
data=pd.read_csv('D:\housePredictionProject\Cleaned_data.csv')

loc=st.selectbox('Choose the location',data['location'].unique())
sqft=st.number_input('Enter Total sqft')
beds=st.number_input('Enter No of Bedrooms')
bath=st.number_input('Enter No of Bathrooms')
balc=st.number_input('Enter No of Balconies')

input=pd.DataFrame([[loc,sqft,bath,balc,beds]],columns=['location','total_sqft','bath','balcony','bedrooms'])

if st.button('Predict Price'):
    output=model.predict(input)
    out_str='Price of the House is '+str(output[0]*100000)
    st.success(out_str)
