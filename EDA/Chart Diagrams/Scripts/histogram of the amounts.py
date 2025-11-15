import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from scipy.stats import norm
import numpy as np
username = "your_username"
password = "your_password"
host = "your_host or IP"
port = 3306
name_of_DB = "FraudLens"

encoded_pass = quote_plus(password)
conn_str = f"mysql+pymysql://{username}:{encoded_pass}@{host}:{port}/{name_of_DB}"
engine = create_engine(conn_str)

query = "SELECT Amount FROM creditcard_transactions;"
df = pd.read_sql(query, engine)
amounts = df["Amount"].tolist()
plt.figure(figsize = (8,5))
plt.hist(amounts, bins = 5, density = True, alpha = 0.6, color = 'b', log = True)
mu, sigma = df['Amount'].mean(), df['Amount'].std()
x = np.linspace(df['Amount'].min(), df['Amount'].max(), 100)
plt.plot(x, norm.pdf(x, mu, sigma), 'r', linewidth=2)
plt.title('Transaction Amount Distribution')
plt.xlabel('Amount')
plt.ylabel('Density')
plt.savefig("Transaction Amount Distribution", dpi = 150, bbox_inches = 'tight')