import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("url_blood_donation_forecast.csv")

print(df.head())

# Correctly define features (X) by dropping the target column
X = df.drop("whether he/she donated blood in March 2007", axis=1)
# Correctly define the target variable (y)
y = df["whether he/she donated blood in March 2007"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = RandomForestClassifier()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print(classification_report(y_test, y_pred))
