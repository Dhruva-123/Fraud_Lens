import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = "username"
password = "password"
host = "local or IP"
port = 3306
name_of_DB = "FraudLens"
encoded_pass = quote_plus(password)
engine = create_engine(f"mysql+pymysql://{username}:{encoded_pass}@{host}:{port}/{name_of_DB}")

data = pd.read_sql("SELECT * FROM creditcard_transactions;", engine)
X = data.drop(columns=['Class'])
y = data['Class']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_normal = X_scaled[y == "0"]

contamination = 0.003
clf = IsolationForest(n_estimators=200, contamination=contamination, random_state=42, n_jobs=-1)
clf.fit(X_normal)

pred = clf.predict(X_scaled)
pred_labels = ["0" if p == 1 else "1" for p in pred]

print("Fraud ratio in dataset:", (y == "1").mean())
print(classification_report(y, pred_labels))


### We got:

### 0.18   - > precision
### 0.37   - > recall
### 0.24   - > f1-score
### That is the best we could muster.