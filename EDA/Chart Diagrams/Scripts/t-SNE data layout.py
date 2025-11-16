import pandas as pd
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


username = "root"
password = "Rahuldhruva@123"
host = "localhost"
port = 3306
name_of_DB = "FraudLens"

encoded_pass = quote_plus(password)
conn_str = f"mysql+pymysql://{username}:{encoded_pass}@{host}:{port}/{name_of_DB}"
engine = create_engine(conn_str)

query = """
SELECT v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,
       v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,Class
FROM creditcard_transactions;
"""
df = pd.read_sql(query, engine)
print(len(df))
df_fraud = df[df['Class'] == "1"]
df_nonfraud = df[df['Class'] == "0"].sample(900, random_state=2)
df_sampled = pd.concat([df_fraud, df_nonfraud])
print("Sampled dataset class distribution:")
print(df_sampled['Class'].value_counts())
X = df_sampled.drop(columns=['Class']).values
y = df_sampled['Class'].values
X_scaled = StandardScaler().fit_transform(X)

tsne = TSNE(
    n_components=2,
    perplexity=60,
    learning_rate='auto',
    init='pca',
    random_state=42
)

X_2d = tsne.fit_transform(X_scaled)

plt.figure(figsize=(10, 8))
plt.scatter(X_2d[y == "0", 0], X_2d[y == "0", 1],
            s=8, alpha=0.9, label='Non-Fraud', color= 'blue')
plt.scatter(X_2d[y == "1", 0], X_2d[y == "1", 1],
            s=20, alpha=0.9, label='Fraud', color='red')

plt.legend()
plt.title("t-SNE Visualization (PCA Data): Fraud vs Non-Fraud")

plt.savefig("tsne_fraud_vs_nonfraud.png", dpi=150, bbox_inches='tight')
print("t-SNE plot saved as tsne_fraud_vs_nonfraud.png")
