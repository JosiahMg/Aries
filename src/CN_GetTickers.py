import tushare
import pandas
import datetime

#Step 1. Get tickers online
tickersRawData = tushare.get_stock_basics()
tickers = tickersRawData.index.tolist()

#Step 1. Save the ticker list to a local file
dateToday = datetime.datetime.today().strftime('%y%m%d')
file = '../data/TickerListCN/TickerList_'+dateToday+'.csv'
tickersRawData.to_csv(file)
print('Tickers saved.')
