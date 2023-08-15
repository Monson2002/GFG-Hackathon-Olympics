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
    YOY_country_participation_data = df.drop_duplicates(subset=["Year", "Region"])[
        "Year"].value_counts().reset_index().sort_values(by="Year")
    YOY_country_participation_data.rename(
        columns={"count": "Number of Participating Countries"}, inplace=True)

    return YOY_country_participation_data


def events_over_the_years(df):
    YOY_events_data = df.drop_duplicates(subset=["Year", "Event"])[
        "Year"].value_counts().reset_index().sort_values(by="Year")
    YOY_events_data.rename(columns={"count": "Number of Events"}, inplace=True)

    return YOY_events_data


def athletes_over_the_years(df):
    YOY_atheletes_data = df.drop_duplicates(subset=["Year", "Name"])[
        "Year"].value_counts().reset_index().sort_values(by="Year")
    YOY_atheletes_data.rename(
        columns={"count": "Number of Athletes"}, inplace=True)

    return YOY_atheletes_data


def top_15_countries(df):
    df.drop_duplicates(subset=["NOC", "Games", "Year", "Season",
                       "City", "Sport", "Event", "Medal", "Region"], inplace=True)
    dic = {}
    df.dropna(inplace=True)
    df.groupby("Region").count()["Medal"].sort_values(ascending=False)
    for i in df["Region"].unique():
        temp_df = df[(df['Region'] == i)]
        dic[i] = temp_df["Medal"].count()
    l = sorted(dic.items(), key=lambda x: x[1], reverse=True)[:15]
    labels = []
    values = []
    for i in l:
        labels.append(i[0])
        values.append(i[1])
    return labels, values


def country_analysis_dropdown(df, country):
    country_NOC = df[df["Region"] == country]["NOC"].unique()[0]
    df.drop_duplicates(subset=["NOC", "Games", "Year", "Season",
                       "City", "Sport", "Event", "Medal", "Region"], inplace=True)
    temp_df = df[df["NOC"] == country_NOC]
    final_df = temp_df.groupby("Year").count()["Medal"].reset_index()
    return final_df


def top_15_per_country(df, country):
    temp_df = df[df["Region"] == country]
    temp_df.drop_duplicates(subset=["Team","NOC","Games","Year","Season","City","Sport","Event","Medal","Region"], inplace=True)
    temp_df[temp_df["Sport"] == "Hockey"]
    final_df = temp_df.groupby(by=["Name"])[["Gold","Silver","Bronze"]].sum().sort_values(by=["Gold","Silver","Bronze"],ascending=False).reset_index()
    final_df["Total"] = final_df["Gold"] + final_df["Silver"] + final_df["Bronze"] 
    return final_df.head(15)


def athelete_tally_age_gold_silver_bronze(df):
    athlete_df = df.drop_duplicates(subset=["Name","Sex","Region"])
    gold = athlete_df[athlete_df["Medal"] == "Gold"]["Age"].dropna()
    silver = athlete_df[athlete_df["Medal"] == "Silver"]["Age"].dropna()
    bronze = athlete_df[athlete_df["Medal"] == "Bronze"]["Age"].dropna()
    l = [gold, silver, bronze]
    return l

def athelete_age_vs_sport(df):
    athlete_df = df.drop_duplicates(subset=["Name","Sex","Region"])
    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)
        
    return x, name