# -*- coding: utf-8 -*-
"""ML project file

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jDZfAvcT8rJrs6P2wVByTCqrIVZ-2NOC
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('/content/Credit_default_dataset.csv')

data.dropna(inplace=True)

X = data.drop('default.payment.next.month', axis=1)
y = data['default.payment.next.month']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

linear_reg = LinearRegression()
linear_reg.fit(X_train_scaled, y_train)
linear_reg_pred = linear_reg.predict(X_test_scaled)
linear_reg_pred_labels = [1 if pred >= 0.5 else 0 for pred in linear_reg_pred]

logistic_reg = LogisticRegression()
logistic_reg.fit(X_train_scaled, y_train)
logistic_reg_pred = logistic_reg.predict(X_test_scaled)

decision_tree = DecisionTreeClassifier()
decision_tree.fit(X_train_scaled, y_train)
decision_tree_pred = decision_tree.predict(X_test_scaled)

def evaluate_model(name, y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    print(f"{name} Evaluation:")
    print(f"Accuracy: {accuracy:.2f}, Precision: {precision:.2f}, Recall: {recall:.2f}, F1 Score: {f1:.2f}")
    return accuracy, precision, recall, f1

linear_accuracy, linear_precision, linear_recall, linear_f1 = evaluate_model("Linear Regression", y_test, linear_reg_pred_labels)
logistic_accuracy, logistic_precision, logistic_recall, logistic_f1 = evaluate_model("Logistic Regression", y_test, logistic_reg_pred)
decision_tree_accuracy, decision_tree_precision, decision_tree_recall, decision_tree_f1 = evaluate_model("Decision Tree", y_test, decision_tree_pred)

plt.figure(figsize=(8, 6))
plt.bar(metrics, scores["Linear Regression"], color='skyblue')
plt.xlabel('Metrics')
plt.ylabel('Scores')
plt.title('Linear Regression Evaluation Metrics')
plt.show()

plt.figure(figsize=(8, 6))
plt.bar(metrics, scores["Logistic Regression"], color='salmon')
plt.xlabel('Metrics')
plt.ylabel('Scores')
plt.title('Logistic Regression Evaluation Metrics')
plt.show()

plt.figure(figsize=(8, 6))
plt.bar(metrics, scores["Decision Tree"], color='lightgreen')
plt.xlabel('Metrics')
plt.ylabel('Scores')
plt.title('Decision Tree Evaluation Metrics')
plt.show()