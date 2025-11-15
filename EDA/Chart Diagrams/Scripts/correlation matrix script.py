import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = "your_username"
password = "your_password"
host = "host or IP"
port = 3306
name_of_DB = "FraudLens"

encoded_pass = quote_plus(password)
con_str = f"mysql+pymysql://{username}:{encoded_pass}@{host}:{port}/{name_of_DB}"
engine = create_engine(con_str)
query = "SELECT v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28 FROM creditcard_transactions;"

df = pd.read_sql(query, engine)
corr_matrix = df.corr()
## We are changing the entire dimensionality of this table because in MySQL, queries are far more easier if we can just type 'WHERE col1 = X and Col2 = Y' rather than finding the columns awkwardly. 
corr_long = corr_matrix.reset_index().melt(id_vars='index')
corr_long.columns = ['col1','col2','correlation']
corr_long.to_sql('correlation_table', con=engine, if_exists='replace', index=False)