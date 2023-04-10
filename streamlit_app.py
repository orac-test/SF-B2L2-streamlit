import streamlit
import pandas

my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Menu options - Breakfast')
streamlit.text('Omega 3 & blueberry oatmeal')
streamlit.text('Zeytin')
streamlit.text('Panir')
streamlit.text('Yumurta')

streamlit.text('🥣 🥗 🐔 🥑🍞')

streamlit.text('Build your own fruit smoothie!') 

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)



