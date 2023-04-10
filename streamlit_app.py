import streamlit
import pandas

my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Menu options - Breakfast')
streamlit.text('Omega 3 & blueberry oatmeal')
streamlit.text('Zeytin')
streamlit.text('Panir')
streamlit.text('Yumurta')

streamlit.text('🥣 🥗 🐔 🥑🍞')

streamlit.text('Build your own fruit smoothie!') 

streamlit.multiselect("Pick some fruits:", list(my_fruits.index))

streamlit.dataframe(my_fruit_list)



