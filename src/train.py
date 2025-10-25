import pandas as pd
import yaml, json
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error
from sklearn.linear_model import LinearRegression

params = yaml.safe_load(open("params.yaml"))
df = pd.read_csv("data/processed.csv")

X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=params["split"]["test_size"],
    random_state=params["split"]["random_state"]
)

models_cfg = params["models"]
results = {}
best_model = None
best_score = -1
best_name = ""

for name, cfg in models_cfg.items():
    if name == "linear_regression":
        model = LinearRegression()
    else:
        continue

    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    score = root_mean_squared_error(y_test, preds)

    results[name] = {"RMSE": score}

    if score > best_score:
        best_score = score
        best_model = model
        best_name = name

joblib.dump(best_model, "model.pkl")
json.dump(results, open("metrics.json", "w"), indent=4)
print(f"El mejor modelo es: {best_name} con un RMSE de {best_score:.4f}")
