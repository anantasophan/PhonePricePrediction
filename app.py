import streamlit as st
import pandas as pd
import pickle

st.title("Phone Price Prediction")

# import model
model = pickle.load(open("phoneprice_pred.pkl", "rb"))

st.write('Insert feature to predict')

# user input
Resolution_x = st.slider(label='Resolution x', min_value=240, max_value=2160, value=1000, step=100)
Resolution_Y = st.slider(label='Resolution y', min_value=320, max_value=3840, value=1000, step=100)
RAM_Size = st.number_input(label='RAM (MB)', min_value=64, max_value=12000, value=500, step=64)
Storage = st.number_input(label='Internal storage (GB)', min_value=4, max_value=512, value=64, step=10)
Screen = st.number_input(label='Screen size (inches))', min_value=2.4, max_value=7.3, value=7.3, step=1.0, format="%.2f")
Camera = st.number_input(label='Rear camera', min_value=0, max_value=108, value=50, step=1)
Brand  = st.selectbox(label='Brand', options=['Apple', 'Samsung', 'Google', 'OnePlus', 'Motorola', 'Others'], key=0)

# convert into dataframe
data = pd.DataFrame({'Resolution x': [Resolution_x],
                'Resolution y': [Resolution_Y],
                'RAM (MB)': [RAM_Size],
                'Internal storage (GB)':[Storage],
                'Screen size (inches)': [Screen],
                'Rear camera': [Camera],
                'Brand': [Brand]})


# model predict
clas = model.predict(data).tolist()[0]
st.write('Price Prediction Result: ', clas, 'Rupees')

