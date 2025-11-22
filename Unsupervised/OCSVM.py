import pandas as pd
from sklearn.svm import OneClassSVM
from sklearn.metrics import classification_report
from sklearn.kernel_approximation import Nystroem
from sklearn.pipeline import make_pipeline
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

X_normal = X[y == "0"]
n_samples = 20000
X_normal_sampled = X_normal.sample(n=n_samples, random_state=42)

feature_map_nystroem = Nystroem(gamma=0.05, n_components=100, random_state=42)
ocsvm = make_pipeline(feature_map_nystroem, OneClassSVM(kernel='linear', nu=0.01))
ocsvm.fit(X_normal_sampled)

pred = ocsvm.predict(X)
pred_labels = ["0" if p == 1 else "1" for p in pred]


print("Fraud ratio in dataset:", (y == "1").mean())
print(classification_report(y, pred_labels))

### This model utterly failed to pickup the patterns of the smaller group. we got ~ 0% prediction rate for class = 1. 
### The model considered all data as class = 0