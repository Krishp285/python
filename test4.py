from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X, y = iris.data, iris.target
model = KNeighborsClassifier(n_neighbors=5)

print("Hold-Out Method (5 Runs with random_state=1)\n")

for i in range(5):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=1)
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    print(f"Run {i+1} Accuracy: {acc:.4f}")

from sklearn.model_selection import cross_val_score
import numpy as np

k_values = [3, 5, 10]

for k in k_values:
    scores = cross_val_score(model, X, y, cv=k)
    print(f"K = {k}")
    print(f"Scores: {scores}")
    print(f"Average Accuracy: {scores.mean():.4f}\n")