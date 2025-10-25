import pandas as pd
import yaml

params = yaml.safe_load(open("params.yaml"))
df = pd.read_csv(params["data"]["input"])

df = df.drop_duplicates()

df.to_csv("data/processed.csv", index=False)
print("Datos procesados y almacenados en data/processed.csv")