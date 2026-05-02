import pandas as pd

df = pd.read_csv("dane.csv", sep = ";")
print(df)

df["Marża"] = (df["Sprzedaż"] - df["Koszt"]) / df["Sprzedaż"]
print(df)

kol = df.loc[(df["Kraj"] == "DE") & (df["Rok"] >= 2023), ["Sprzedaż", "Marża"]]

print(kol)