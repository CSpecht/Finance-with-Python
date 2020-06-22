from financeAPI import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from urllib.request import urlopen
from google.cloud import storage
import os
from io import StringIO 
from datetime import date

with open('C:\Scripts\Secret_Key.txt') as f: 
    key = f.read()
    f = FinanceAPI()
    f.registerKey_(key)
    
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\Scripts\DataWarehouseWorkshop_Key.json'

apple_dict = f.build_dict('AAPL')
df = f.build_dataframe(['GOOG','AMZN','ATVI','EBAY','PYPL','TSLA','COKE','WMT','DB','GE','GM','MS','SAP','NKE','NFLX','AAPL','TWTR','FB','MA','CRM','MCD'])
# comment in for having a dateNow column
# df['dateNow'] = date.today()
fs = StringIO()
df.to_csv(fs)
fs.seek(0)
gcs = storage.Client()
gcs.bucket('dww_data_finance').blob('financeData.csv').upload_from_file(fs,content_type='text/csv')

forex = pd.DataFrame(f.forex_data_('EUR','USD'))
fx = StringIO()
forex.to_csv(fx)
fx.seek(0)
gcs = storage.Client()
gcs.bucket('dww_data_finance').blob('currency.csv').upload_from_file(fx,content_type='text/csv')


#print(df)
