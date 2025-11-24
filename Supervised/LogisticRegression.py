import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, precision_recall_curve, average_precision_score
import numpy as np
import joblib
### In this section, we will be grabbing data from the SQL table. Nothing new here, we have seen this exact thing in other files as well.
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

### Now that we have the data, we are now going to change the Class from string to integers because that is far more easy for us to evaluate later
data["Class"] = data["Class"].astype(str).str.strip()
data["Class"] = data["Class"].replace({"0": 0, "1": 1})
data["Class"] = data["Class"].astype(int)

### We are taking fraud data and non fraud data in 1:10 ratio to train the data because otherwise, the model cannot properly train on 0.017% of one class and the rest in another class.
### We are also taking only a sample of around half the number of fraud data because we don't want to overfit the model with every fraud and not every non-fraud.
fraud_data = data[data["Class"] == 1].sample(200, random_state=42)
non_fraud_data = data[data["Class"] == 0].sample(len(fraud_data)*10, random_state=42)
train_data = pd.concat([fraud_data, non_fraud_data])

X_train = train_data.drop(columns=["Class"])
y_train = train_data["Class"]

X_test = data.drop(columns=["Class"]).drop(non_fraud_data.index)
y_test = data["Class"].drop(non_fraud_data.index)

### Although the dataset we got doesn't need scaling, we are doing it anyway because it's standard practice.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


### Actual training of the model
lr = LogisticRegression(class_weight="balanced", max_iter=500)
lr.fit(X_train_scaled, y_train)
joblib.dump(lr, r"D:\AI\fraudlens\FraudLens\API\Models\LogisiticRegression.pkl")
### Getting predictions
y_scores = lr.predict_proba(X_test_scaled)[:,1]

### Using precision recall curve to get proper thresholds and it will later be used to find the best threshold.
precision, recall, thresholds = precision_recall_curve(y_test, y_scores)
f1_scores = 2*precision*recall/(precision+recall+1e-8)
best_idx = np.argmax(f1_scores)
best_threshold = thresholds[best_idx]
y_pred = (y_scores >= best_threshold).astype(int)


print(f"Best threshold for fraud detection: {best_threshold:.4f}")
print(f"PR-AUC: {average_precision_score(y_test, y_scores):.4f}")
print(classification_report(y_test, y_pred, digits=4))

#### The result we got.
'''
Best threshold for fraud detection: 0.9965
PR-AUC: 0.7193
              precision    recall  f1-score   support

           0     0.9997    0.9994    0.9995    282315
           1     0.6870    0.8028    0.7404       492

    accuracy                         0.9990    282807
   macro avg     0.8433    0.9011    0.8700    282807
weighted avg     0.9991    0.9990    0.9991    282807
'''