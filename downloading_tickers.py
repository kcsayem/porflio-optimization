import pandas as pd

tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
df = tables[0]['Symbol']
print(df)
df.to_pickle('Data/sp500Ticker.pickle',  compression='infer')
# df = pd.read_pickle('Data/DowJonesTicker.pickle')
# print(df.head())