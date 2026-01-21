import pickle
import pandas as pd
import streamlit as st

#load the data
df = pd.read_csv("Cleaned_df.csv")

#load pre-trained model
with open("RF_model.pkl","rb") as file:
    model = pickle.load(file)

# page setup
st.set_page_config(page_icon="🏠",page_title="House Price Prediction",layout="wide")

st.header("🏡 SmartEstimate")

with st.sidebar:
    st.title("House price prediction")
    #st.image("https://img.freepik.com/premium-vector/logo-house-logo-that-says-house-logo-it_1280538-650.jpg?semt=ais_hybrid&w=740&q=80",width=250)
    st.image("Modern_house.png",width=250)


def get_encoded_loc(location):
    for loc,encoded in  zip(df["location"],df["encoded_loc"]):
        if location==loc:
            return encoded

#user input:  location,bhk,bath,total sqft
pred = None
with st.container(border=True):
    c1,c2 = st.columns(2)
    with c1:
        location = st.selectbox("📌 Location : ",options=df["location"].unique())
        bhk = st.selectbox("🛏️ BHK : ",options=sorted(df["bhk"].unique()))

    with c2:
        bath = st.selectbox("🛁 No.of. Bathrooms : ",options=sorted(df["bath"].unique()))
        sqft = st.number_input("📐 Total Sqft : ",min_value=300)
    #convert str loc into encoded loc
    location= get_encoded_loc(location)
    a1,a2,a3 = st.columns([1.5,1,1])
    #Price prediction
    if a2.button("Predict Price"):
        data = [[sqft,bath,bhk,location]] # data as 2D
        pred = model.predict(data)[0] #predicts price
        pred = f"{pred*100000:.2f}"

if pred is not None:
    st.subheader(f"Predicted Price: Rs. {pred}")