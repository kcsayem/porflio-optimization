import pandas as pd
from pandas_datareader import data
from tqdm import tqdm

tickers =  pd.read_pickle('Data/sp500Ticker.pickle')

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2009-01-01'
end_date = '2019-12-31'
delete_tickers = ['AAPl', 'AMGN']

# for ticker in tqdm(tickers):
#     try:
#         panel_data = data.DataReader(ticker, 'yahoo', start_date, end_date)
#         panel_data.to_csv('Data/sp500/' + ticker + '.csv')
#     except:
#         delete_tickers.append(ticker)

tickers = tickers.remove(delete_tickers)
print(tickers)
# tickers.to_pickle('Data/sp500Ticker.pickle',  compression='infer')
# ticker = '^TNX'
# panel_data = data.DataReader(ticker, 'yahoo', start_date, end_date)
# panel_data.to_csv('Data/Bonds/' + ticker + '.csv')


