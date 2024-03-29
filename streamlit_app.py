import pandas
import streamlit
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

def get_fruitvise_data(this_fruit_choice):
 fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
 fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
 return fruityvice_normalized
  #header
streamlit.header("Fruityvice Fruit Advice!")
try:
 fruit_choice = streamlit.text_input('What fruit would you like information about?')
 if not fruit_choice:
    streamlit.error("Please select a fruit to get information:")
 else:
   back_from_function = get_fruityvise_data(fruit_choice)
   streamlit.dataframe(back_from_function)
except URLError as e:
     streamlit.error()


streamlit.header("The fruit load contains!")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

  if streamlit.button('Get fruit load list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows= get_fruit_load_list()
   streamlit.dataframe(my_data_rows)

streamlit.stop()

def nsert_row_snowflake(new_fruit):
 with my_cnx.cursor() as my_cur:
  my_cur.execute("insert into fruit_load_list values ('from streamlit')")
  return "Thanks for adding "+new_fruit
  
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the list'):
 my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
 back_fron_function=insert_row_snowflake(add_my_fruit)
 streamlit.text(back_fron_function)

# streamlit.text("The fruit load list")
# streamlit.text(my_data_row)

# my_data_row = my_cur.fetchall()
# streamlit.header("Hello from Snowflake:")
# streamlit.dataframe(my_data_row)

# streamlit.write('Thanks for adding',add_my_fruit)


