import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

# create a data viewer
st.header("Select Vehicle")
st.dataframe(df)

# visualize vehicle price by manufacturer
st.header('Vehicle price by manufacturer')
price_per_manu = px.histogram(df, x='price',color='manufacturer')
st.write(price_per_manu)
manu_checker = st.checkbox('manufacturer')

# Visualize vehicle price base on mileage on odometer
st.header('Vehicle price by milleage')
fig_odometer_price = px.scatter(df, x='odometer', y='price', labels={'odometer': 'Odometer (miles)', 'price': 'Price ($)'})
st.write(fig_odometer_price)