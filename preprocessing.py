import pandas as pd

def preprocess(file_name, test=False):

    if test==False:
        fake_date_range = pd.date_range(start="01/01/2017", end="30-12-2022")
    else:
        fake_date_range = pd.date_range(start="01/01/2023", end="30-12-2024")
    
    target='rainfall'

    df = pd.read_csv(file_name, index_col=0)

    df['year'] = 0
    for i in range(6):
        df.loc[i*365:(i+1)*365, 'year'] = i
    
    df['date'] = fake_date_range
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month

    def get_season(month):
        if month in [12, 1, 2]:
            return 0 # Winter
        elif month in [3, 4, 5]:
            return 1 # Spring
        elif month in [6, 7, 8]:
            return 2 # Summer
        elif month in [9, 10, 11]:
            return 3 # Autumn
        else:
            return 'Unknown'

    # Appliquer la fonction pour obtenir la saison
    df['season'] = df['month'].apply(get_season)

    df.drop(columns=['date'], inplace=True)

    if test==True:
        return df

    X = df.drop(columns=[target])
    y = df[target]

    return X, y

