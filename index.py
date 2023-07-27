import streamlit as st
import pandas as pd
from Analysis import preprocess
import helper

df = pd.read_csv("./Datasets/medals.csv")

df = preprocess(df)

st.sidebar.title("Olympics Analysis")

clicked_option = st.sidebar.radio(
    "Select an option:",
    ("Medal Tally", "Overall Analysis",
     "Country-wise Analysis", "Athlete-wise Analysis")
)

st.sidebar.header("Filters")

dropdown_year = st.sidebar.selectbox(
    "Select Year", helper.year_dropdown(df)
)

dropdown_country = st.sidebar.selectbox(
    "Select Country", helper.country_dropdown(df)
)


if clicked_option == "Medal Tally":
    if dropdown_country == "Country" and dropdown_year == "Year":
        st.header("Overall Tally")
    elif dropdown_country != "Country" and dropdown_year == "Year":
        st.header(dropdown_country)
    elif dropdown_country == "Country" and dropdown_year != "Year":
        st.header("Medal Tally in " + dropdown_year + f" ")
    else:
        st.header(dropdown_country + " in " + dropdown_year)
    x = helper.fetch_medal_tally(df, dropdown_year, dropdown_country)
    st.table(x)

    # dropdown_year
    # dropdown_country

if clicked_option == "Overall Analysis":
    st.header("Analysis of Overall Games")
    
    col1, col2, col3 = st.columns(3)
    x = helper.no_of_editions(df)
    with col1:
        st.subheader("Editions: ")
        st.title(x)

    x = helper.no_of_cities(df)
    with col2:
        st.subheader("Cities: ")
        st.title(x)

    x = helper.no_of_events(df)
    with col3:
        st.subheader("Events: ")
        st.title(x)
    
    col1, col2 = st.columns(2)
    x = helper.no_of_atheletes(df)
    with col1:
        st.subheader("Atheletes: ")
        st.title(x)

    x = helper.no_of_participating_nations(df)
    with col2:
        st.subheader("Nations: ")
        st.title(x)

