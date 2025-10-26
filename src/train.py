import pandas as pd
import yaml, json
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

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
best_score = float('inf') # Inicializando con infinito, mas bajo mejor.
best_name = ""

for name, cfg in models_cfg.items():
    if name == "linear_regression":
        model = LinearRegression()
    elif name == "random_forest_regressor":
        model = RandomForestRegressor(**cfg)
    elif name == "gradient_boosting_regressor":
        model = GradientBoostingRegressor(**cfg)
    else:
        continue

    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    score = root_mean_squared_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    mscore = mean_squared_error(y_test, preds)

    results[name] = {"RMSE": score, "R2": r2, "MSE": mscore}

    if score < best_score:
        best_score = score
        best_model = model
        best_name = name

joblib.dump(best_model, "model.pkl")
json.dump(results, open("metrics.json", "w"), indent=4)
print(f"El mejor modelo es: {best_name} con: \nRMSE de {best_score:.4f} \nR2 de {results[best_name]['R2']:.4f} \nMSE de {results[best_name]['MSE']:.4f}")
