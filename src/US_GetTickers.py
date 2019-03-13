import tushare
import io
import datetime
import pandas
import requests

#Step 1. Get ticker list online

url = 'http://www.nasdaq.com/screening/     \
       companies-by-industry.aspx?exchange=NASDAQ&render=download'

dataString = requests.get(url).content


tickersRawData = pandas.read_csv(io.StringIO(dataString.decode('utf-8')), error_bad_lines=False)
print(tickersRawData)

tickers = tickersRawData['Symbol'].tolist()

dateToday = datetime.datetime.today().strftime('%y%m%d')
#Step 2. Save the ticker list to a local file
file = '../data/TickerListUS/TickerList_'+dateToday+'.csv'
tickersRawData.to_csv(file, index=False)
print('Tickers saved')
