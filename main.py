import streamlit as st
import pandas as pd
import helper


df=pd.read_csv('matches_1930_2022.csv')
ef=pd.read_csv('fifa_ranking_2022-10-06.csv')
ff=pd.read_csv('world_cup.csv')

st.sidebar.title("Football Analysis")
user_menu=st.sidebar.radio(
    'Select an option',('Most world cup winners','Country wise Analysis','Year wise','Goals')
)



if user_menu == 'Most world cup winners':
    #a is use wc winner no.
    a=helper.most_winner(ff)
    st.table(a)


if user_menu == 'Country wise Analysis':

    st.sidebar.title("Country wise Analysis")
    country_list=ef['team'].unique().tolist()
    country_list.sort()
    country_list.insert(0,'overall')

    selected_country=st.sidebar.selectbox('Select a Country',country_list)

    if selected_country == 'overall':
        b = helper.countrywise_ana(ef)
        st.table(b)

if user_menu == 'Year wise':
    st.sidebar.title("Year wise Analysis")
    year_list = ff['Year'].unique().tolist()
    year_list.sort()

    selected_year = st.sidebar.selectbox('Select a Year', year_list)

    c = helper.yearwise_ana(ff, selected_year)
    if selected_year != 'overall':
        st.title("Year wise :")
        st.dataframe(c)




    st.sidebar.title("Host wise Analysis")
    host_list = ff['Host'].unique().tolist()
    host_list.sort()

    selected_host = st.sidebar.selectbox('Select a Host', host_list)

    d = helper.hostwise_ana(ff, selected_host)
    if selected_host != 'overall':
        st.title("Host wise :")
        st.dataframe(d)




