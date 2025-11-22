import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = "username"
password = "password"
host = "local or IP"
port = 3306
name_of_DB = "FraudLens"

encoded_pass = quote_plus(password)
con_str = f"mysql+pymysql://{username}:{encoded_pass}@{host}:{port}/{name_of_DB}"
engine = create_engine(con_str)

query = "SELECT * FROM creditcard_transactions;"
data = pd.read_sql(query, engine)


X = data.drop(columns=['Class'])
y = data['Class']


kmeans = KMeans(n_clusters=2, random_state=42)
pred_labels = kmeans.fit_predict(X)

ari = adjusted_rand_score(y, pred_labels)
print("Adjusted Rand Index:", ari)

### I think we all knew that K-means would fail badly here. We ofc got a score of zero here. K-Means only works well when the dataset is balanced and the clusterings are spherical in nature.
### From our t-SNE graph, I assume that supervised models would do a better job at picking things up because it feels like the data is lineraly seperable to some degree.