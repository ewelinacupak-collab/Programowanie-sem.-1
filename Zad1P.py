import pandas as pd

df = pd.read_csv("dane.csv", sep = ";")
print(df)

df["Marża"] = (df["Sprzedaż"] - df["Koszt"]) / df["Sprzedaż"]

print(df)

df = df.sort_values(by = ["Rok", "Kraj"],
                    ascending = [True, True])

print(df)