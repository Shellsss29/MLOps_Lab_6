import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

print("Training model...")

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

acc = model.score(X_test, y_test)
print(f"Model trained! Accuracy: {acc:.4f}")

with open("/model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Saved model to /model/model.pkl")
