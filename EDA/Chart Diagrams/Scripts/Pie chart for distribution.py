import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

## We are storing our data in variables to be able to run this engine and get the required SQL data.
DB_USER = "your_username"
DB_PASS = "your_password"
DB_HOST = "host or IP"
DB_PORT = 3306
DB_NAME = "FraudLens"

encoded_pass = quote_plus(DB_PASS) ## We are encoding the password so that it wont lead to syntax problems
conn_str = f"mysql+pymysql://{DB_USER}:{encoded_pass}@{DB_HOST}:{DB_PORT}/{DB_NAME}" ## We are creating and string here doing mysql+pymysql and then giving it your data in order to get access to our DB
engine = create_engine(conn_str)

query = "SELECT Class, COUNT(*) AS cnt FROM creditcard_transactions GROUP BY Class;"
df = pd.read_sql(query, engine) ##read_sql function takes query that we want and the data and engine and it runs the query and gets our data and stores it as a pandas frame.

label_map = {0: "Non-Fraud (Class 0)", 1: "Fraud (Class 1)"} ## This is just labeling the data we got.
df['label'] = df['Class'].map(label_map).fillna(df['Class'].astype(str))

sizes = df['cnt'].tolist()
labels = df['label'].tolist()

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=90, colors=['#66b3ff','#ff6666'])
plt.title('Class Distribution — creditcard_transactions')
plt.axis('equal') ##This creates a closed circle properly.
plt.savefig('class_distribution_pie.png', dpi=150, bbox_inches='tight')
# plt.show()  # optional, can comment out
