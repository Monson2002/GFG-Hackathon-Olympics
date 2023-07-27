import pandas as pd


def medal_tally(df):
    medal_tally = df.groupby("country_name").sum(numeric_only=True)[["GOLD", "SILVER", "BRONZE"]].sort_values(
        by=["GOLD", "SILVER", "BRONZE"], ascending=[False, False, False]).reset_index()
    medal_tally["Total"] = medal_tally["GOLD"] + \
        medal_tally["SILVER"] + medal_tally["BRONZE"]
    return medal_tally


def year_dropdown(df):
    years = df["slug_game"].str[-4:].unique().tolist()
    years.insert(0, "Year")
    return years


def country_dropdown(df):
    country = df["country_name"].unique().tolist()
    country.insert(0, "Country")
    return country


def fetch_medal_tally(df, year, country):
    flag = 0
    if country == "Country" and year == "Year":
        temp_df = df
    elif country != "Country" and year == "Year":
        flag = 1
        temp_df = df[df["country_name"] == country]
    elif country == "Country" and year != "Year":
        temp_df = df[df["slug_game"].str[-4:] == year]
    else:
        temp_df = df[(df["country_name"] == country) &
                     (df["slug_game"].str[-4:] == year)]

    if flag == 1:
        x = temp_df.groupby("year").sum(numeric_only=True)[
            ["GOLD", "SILVER", "BRONZE"]]
        x.sort_values(by="year", ascending=False, inplace=True)
        x.reset_index(inplace=True)
    else:
        x = temp_df.groupby("country_name").sum(numeric_only=True)[["GOLD", "SILVER", "BRONZE"]].sort_values(
            by=["GOLD", "SILVER", "BRONZE"], ascending=[False, False, False]).reset_index()
    x["TOTAL"] = x["GOLD"] + x["SILVER"] + x["BRONZE"]
    return x


def no_of_editions(df):
    return len(df["year"].unique().tolist())


def no_of_cities(df):
    no_of_cities = []
    for i in list(df["slug_game"].unique().tolist()):
        if len(i.split("-")) > 2:
            no_of_cities.append([i[:-5]])
        else:
            no_of_cities.append(i.split("-")[:-1])
    return len(no_of_cities)


def no_of_events(df):
    return len(df["discipline_title"].unique().tolist())

def no_of_atheletes(df):
    return len(df["athlete_full_name"].unique().tolist())

def no_of_participating_nations(df):
    return len(df["country_3_letter_code"].unique().tolist())
