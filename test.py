import pandas as pd

df = pd.read_csv('Data/tickersWithMoney.csv')

for row in range(0, len(df)):
    print(df.iloc[row]['tickers'], df.iloc[row]['money'])