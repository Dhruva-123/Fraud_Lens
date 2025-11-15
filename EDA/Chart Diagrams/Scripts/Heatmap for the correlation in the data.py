import pandas as pd
import seaborn as sns
from urllib.parse import quote_plus
from sqlalchemy import create_engine 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

username = "root"
password = "Rahuldhruva@123"
host = "localhost"
port = 3306
name_of_DB = "FraudLens"
encoded_pass = quote_plus(password)
con_str = f"mysql+pymysql://{username}:{encoded_pass}@{host}:{port}/{name_of_DB}"
engine = create_engine(con_str)
query = "SELECT * FROM correlation_table;"  # make sure it has ['col1','col2','correlation']
df = pd.read_sql(query, engine)
matrix = df.pivot(index='col1', columns='col2', values='correlation')
cols = [f"v{i}" for i in range(1,29)]  # ensures v1..v28 order
matrix = matrix.loc[cols, cols]

plt.figure(figsize=(12,10))
sns.heatmap(
    matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    cbar=True
)
plt.title("Correlation Heatmap (v1-v28)")
plt.tight_layout()
plt.savefig("Correlation Heatmap (v1-v28)", dpi = 150, bbox_inches = 'tight')
