import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://newuser:password@localhost:5432/postgres')

play_list = ['AAPL','MSFT','GOOG','AMZN','NVDA','TSLA','META','LLY',
             'V','XOM','UNH','WMT','JPM','MA','JNJ','PG','AVGO','ORCL','HD',
             'CVX','MRK','ABBV','ADBE','KO','COST','PEP','CSCO','BAC','CRM',
             'MCD','TMO','NFLX','PFE','CMCSA','DHR','ABT','AMD','TMUS','INTC',
             'INTU','WFC','TXN','NKE','DIS','COP','CAT','PM','MS','VZ','AMGN',
             'UPS','NEE','IBM','LOW','UNP','BA','BMY','SPGI','AMAT','HON',
             'NOW','GE','RTX','QCOM','AXP','DE','PLD','SYK','SBUX',
             'SCHW','GS','LMT','ELV','ISRG','TJX','BLK','T','ADP','UBER',
             'MMC','MDLZ','GILD','ABNB','REGN','LRCX','VRTX','ADI','ZTS',
             'SLB','CVS','AMT','CI','BX','PGR','BSX','MO','C','BDX']

sql = 'SELECT * FROM df_m60;'
df = pd.read_sql(sql, con=engine)

sym_dct = {}
for symbol in play_list:
    df_tmp = pd.concat([df[f'{symbol}_Open'],
                        df[f'{symbol}_High'],
                        df[f'{symbol}_Low'],
                        df[f'{symbol}_Close'],
                        df[f'{symbol}_Volume']],axis=1).to_numpy(np.float32)
    sym_dct[symbol] = df_tmp
    
AAPL = sym_dct["AAPL"]
