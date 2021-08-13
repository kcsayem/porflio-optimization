import backtrader as bt
from datetime import datetime, timedelta, date
from algorithimic-trading-backtrading import RSIStrategy, SMAStrategy, TestStrategy
import pandas as pd
import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])




tickers = pd.read_pickle('Data/DowJonesTicker.pickle')
df = pd.read_csv('Data/tickersWithMoney.csv')
invest = 0
final = 0
for row in range(0, len(df)):
    ticker = df.iloc[row]['tickers'] 
    cash = float(df.iloc[row]['money'])
    if cash > 0:
        # Create a cerebro entity
        cerebro = bt.Cerebro()

        # Add a strategy
        cerebro.addstrategy(SMAStrategy)

        modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
        temp = 'Data/Stocks/dow_jones/' + ticker + '.csv'
        datapath = os.path.join(modpath, temp)

        data = pd.read_csv(datapath, index_col='Date', parse_dates=True)
        # data = data[:1000]
        fromdate =  datetime.datetime(2019, 1, 1)
        todate = datetime.datetime(2019, 12, 31)
        feed = bt.feeds.PandasData(dataname=data, fromdate=fromdate, todate=todate)
        cerebro.adddata(feed)

        # Set our desired cash start
        cerebro.broker.setcash(cash)

        # Add a FixedSize sizer according to the stake
        # cerebro.addsizer(bt.sizers.PercentSizerInt, percents=100)

        # # Set the commission - 0.1% ... divide by 100 to remove the %
        # cerebro.broker.setcommission(commission=0)

        # Print out the starting conditions
        print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

        # Run over everything
        cerebro.run()

        # Print out the final result
        print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
        invest += cash
        final += cerebro.broker.getvalue()
        # Finally plot the end results
        # cerebro.plot(style='candlestick') 

print('Total Invested Amount ', invest, ' & final amount ', final)
print('Total Profit in 2019:', (final - invest)/invest)
