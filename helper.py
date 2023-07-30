import pandas as pd


def fetch_medal_tally(df, year, country):
    flag = 0
    if country == "Region" and year == "Year":
        temp_df = df
    elif country != "Region" and year == "Year":
        temp_df = df[df["Region"] == country]
        flag = 1
    elif country == "Region" and year != "Year":
        temp_df = df[df["Year"] == year]
    else:
        temp_df = df[(df["Region"] == country) & (df["Year"] == year)]
    if flag == 1:
        df = temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal', 'Region']).groupby(
            "Year").sum(numeric_only=True)[["Gold", "Silver", "Bronze"]].sort_values(by="Year", ascending=False).reset_index()
    else:
        df = temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal', 'Region']).groupby(
            "Region").sum()[["Gold", "Silver", "Bronze"]].sort_values(by=["Gold"], ascending=False).reset_index()
    df["Total"] = df["Gold"] + df["Silver"] + df["Bronze"]

    return df


def year_dropdown(df):
    years = df["Year"].unique().tolist()
    years.sort(reverse=True)
    years.insert(0, "Year")
    return years


def country_dropdown(df):
    region_df = df["Region"].dropna()
    regions = list(set(region_df.unique().tolist()))
    regions.sort()
    regions.insert(0, "Region")
    return regions


def no_of_editions(df):
    return len(df["Year"].unique().tolist())


def no_of_cities(df):
    return df["City"].unique().size


def no_of_events(df):
    return len(df["Sport"].unique().tolist())


def no_of_atheletes(df):
    return len(df["Name"].unique().tolist())


def no_of_participating_nations(df):
    return len(df["Region"].unique().tolist())

def nations_over_the_years(df):
    YOY_country_participation_data = df.drop_duplicates(subset=["Year","Region"])["Year"].value_counts().reset_index().sort_values(by="Year")
    YOY_country_participation_data.rename(columns={"count":"Number of Participating Countries"}, inplace=True)

    return YOY_country_participation_data

def events_over_the_years(df):
    YOY_events_data = df.drop_duplicates(subset=["Year","Event"])["Year"].value_counts().reset_index().sort_values(by="Year")
    YOY_events_data.rename(columns={"count":"Number of Events"}, inplace=True)

    return YOY_events_data

def athletes_over_the_years(df):
    YOY_atheletes_data = df.drop_duplicates(subset=["Year","Name"])["Year"].value_counts().reset_index().sort_values(by="Year")
    YOY_atheletes_data.rename(columns={"count":"Number of Athletes"}, inplace=True)

    return YOY_atheletes_data