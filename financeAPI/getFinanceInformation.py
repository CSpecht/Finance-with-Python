from financeAPI import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from urllib.request import urlopen
from google.cloud import storage
import os
from io import StringIO 

with open('Secret_Key.txt') as f: 
    key = f.read()
    f = FinanceAPI()
    f.registerKey_(key)
    
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\Scripts\DataWarehouseWorkshop_Key.json'

apple_dict = f.build_dict('AAPL')
df = f.build_dataframe(['TWTR','FB','MSFT','NVDA','AAPL','CRM'])

fs = StringIO()
df.to_csv(fs)
fs.seek(0)
gcs = storage.Client()
gcs.bucket('dww_data_finance').blob('financeData.csv').upload_from_file(fs,content_type='text/csv')



print(df)
