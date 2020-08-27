import pandas as pd
from sqlalchemy import create_engine

file = 'myfile_or_filepath.csv'

#preview the file
# sample = pd.read_csv(file, nrows=20)

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


query = """
SELECT * FROM "table" WHERE "Unnamed:0"='id';
"""
df = pd.read_sql_query(query, csv_database)

#gets columns
#SELECT sql FROM sqlite_master WHERE name='table';
#df.sql[0]

#gets connection url
#csv_database.url

#also gets table names
#csv_database.table_names()


