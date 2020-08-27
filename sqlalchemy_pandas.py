import pandas as pd
from sqlalchemy import create_engine

file = '/path/to/csv/file'

#preview the file
pd.read_csv(file, nrows=5)

csv_database = create_engine('sqlite:///csv_database.db')

#break file into chunks
chunksize = 100000
i = 0
j = 1
for df in pd.read_csv(file, chunksize=chunksize, iterator=True):
      df = df.rename(columns={c: c.replace(' ', '') for c in df.columns}) 
      df.index += j
      i+=1
      df.to_sql('table', csv_database, if_exists='append')
      j = df.index[-1] + 1
#dont really want to load the whole db, change select statement below      
df = pd.read_sql_query('SELECT * FROM table', csv_database)
