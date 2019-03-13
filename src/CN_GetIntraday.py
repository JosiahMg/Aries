import tushare
import pandas
import datetime
import os

def stockPriceIntraday(ticker, folder):

    #Step 1 . Get the history data online
    intraday = tushare.get_hist_data(ticker, ktype='5')

    #Step 2 . If the history exists, append
    file = folder+'/'+ticker+'.csv'
    if os.path.exists(file):
        history = pandas.read_csv(file, index_col=0)
        intraday.append(history)
    #Step 3 . Inverse based on index
    intraday.sort_index(inplace=True)
    intraday.index.name = 'timestamp'

    #Step 4 . Save
    intraday.to_csv(file)
    print('Intraday for [' + ticker + '] got.')


tickersRawData = tushare.get_stock_basics()
tickers = tickersRawData.index.tolist()

dateToday = datetime.datetime.today().strftime('%y%m%d')

file = '../data/TickerListCN/TickerList_'+dateToday+'.csv'
tickersRawData.to_csv(file)
print('Tickers saved.')


for i, ticker in enumerate(tickers):
    try:
        print('Intraday', i, '/', len(tickers))
        stockPriceIntraday(ticker, folder='../data/IntradayCN')
    except:
        pass
print('Intraday for all stocks got.')
