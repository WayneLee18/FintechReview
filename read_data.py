import pandas as pd
from sqlalchemy import create_engine


file = 'CRSPDailyStockPrice2004_2018.csv'
sample= pd.read_csv(file, nrows=30)