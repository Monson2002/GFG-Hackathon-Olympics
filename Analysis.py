import pandas as pd

def preprocess(df, df_regions):
    df = df.merge(df_regions, on="NOC", how="left")
    df.drop(df[df["Year"] == 1906].index, inplace=True)
    df = df.rename(columns={"region":"Region", "notes":"Notes"})
    df = df.drop_duplicates()
    df = df[df['Season'] == "Summer"]
    df = pd.concat([df, pd.get_dummies(df["Medal"])], axis=1)
    return df