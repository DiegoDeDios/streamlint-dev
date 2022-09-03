import streamlit as st
import pandas as pd
#data 

sales_data = pd.read_csv("./videogame_sales_2016.csv")
game_publishers = list(sales_data["Publisher"].drop_duplicates())


st.title("Videogame sales data up to 2020")

company = st.multiselect("Company",sales_data["Publisher"].drop_duplicates())

year_range = st.slider("Select time frame",int(sales_data["Year_of_Release"].dropna().astype(int).min()),int(sales_data["Year_of_Release"].dropna().astype(int).max()),(1998,2020))

print(year_range)

st.dataframe(sales_data[(sales_data["Publisher"].isin(company)) & sales_data["Year_of_Release"].isin(year_range)])