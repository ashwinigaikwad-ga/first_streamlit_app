import pandas
import streamlit
import snowflake.connector


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)

streamlit.multiselect(streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)))

