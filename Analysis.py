import pandas as pd

def preprocess(df):
    df = pd.concat([df, pd.get_dummies(df["medal_type"])], axis=1)
    df["year"] = df["slug_game"].str[-4:]
    return df