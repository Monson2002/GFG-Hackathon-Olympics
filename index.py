import streamlit as st
import pandas as pd
from Analysis import preprocess
import helper
import plotly.express as px

df = pd.read_csv("./Datasets/athlete_events.csv")
df_regions = pd.read_csv("./Datasets/noc_regions.csv")

df = preprocess(df, df_regions)

st.sidebar.title("Olympics Analysis")

clicked_option = st.sidebar.radio(
    "Select an option:",
    ("Medal Tally", "Overall Analysis", "Country-wise Analysis", "Athlete-wise Analysis")
)

st.sidebar.header("Filters")

dropdown_year = st.sidebar.selectbox(
    "Select Year", helper.year_dropdown(df)
)

dropdown_country = st.sidebar.selectbox(
    "Select Country", helper.country_dropdown(df)
)


if clicked_option == "Medal Tally":
    if dropdown_country == "Region" and dropdown_year == "Year":
        st.header("Overall Medal Tally")
    elif dropdown_country != "Region" and dropdown_year == "Year":
        st.header(dropdown_country + "'s Overall Medal Tally")
    elif dropdown_country == "Region" and dropdown_year != "Year":
        st.header("Overall Medal Tally in " + str(dropdown_year))
    else:
        st.header(dropdown_country + "'s Medal Tally in " + str(dropdown_year))
    x = helper.fetch_medal_tally(df, dropdown_year, dropdown_country)
    st.table(x)


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
        
    
    st.header("Participating Nations over the years")
    nations_over_the_years = helper.nations_over_the_years(df)
    fig = px.line(nations_over_the_years, x="Year", y="Number of Participating Countries") 
    st.plotly_chart(fig) 

    st.header("Number of Events over the years")
    events_over_the_years = helper.events_over_the_years(df)
    fig = px.line(events_over_the_years, x="Year", y="Number of Events") 
    st.plotly_chart(fig)
    
    st.header("Number of Athletes over the years")
    athletes_over_the_years = helper.athletes_over_the_years(df)
    fig = px.line(athletes_over_the_years, x="Year", y="Number of Athletes") 
    st.plotly_chart(fig) 
    

     
    
    

