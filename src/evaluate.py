import json
import pandas as pd

metrics = json.load(open("metrics.json"))
df = pd.DataFrame(metrics).T
df.to_csv("report.csv")

print("Reporte de metricas guardado en: report.csv")
