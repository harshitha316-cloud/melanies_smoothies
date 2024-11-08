# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie!:cup_with_straw:")
st.write(
          """      
          choose the fruits you want in custom smoothie!
        """
)

#import streamlit as st

cnx=st.connection("snowflake")
session=cnx.session()

name_on_order = st.text_input('Name on Smoothie:')
st.write('The name on your smoothie will be :', name_on_order)

#option = st.selectbox(
#    "What is your favorite fruit?",
#    ("Strawberry", "Banana", "Peaches"),
#)

#st.write("You selected:", option)



#session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('fruit_name'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list=st.multiselect(
    'Choose up to 5 ingredients:'
    ,my_dataframe
    ,max_selections=5
)
if ingredients_list:
   # st.write(ingredients_list)
    #st.text(ingredients_list)

    ingredients_string = ''
    
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
    st.write(ingredients_string)
ingredients_string = ''
my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
      values ('""" +ingredients_string+ """','""" + name_on_order+ """')"""

#st.write(my_insert_stmt)
#st.stop()

time_to_insert = st.button('Submit Order')

if time_to_insert:
   session.sql(my_insert_stmt).collect()
    
   Succcess_message = 'Your Smoothie is Ordered '+name_on_order+'!'
    
   st.success(Succcess_message,icon="✅")
   #st.success('Your Smoothie is ordered' ,icon="✅")
   #st.success(Messg ,icon="✅")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#st.text(fruityvice_response.json())
fv_df=st.dataframe(data=fruityvice_response.json(),use_container_width=True)
