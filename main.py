import pandas as pd

df = pd.read_csv("data/results.csv")

wpm_media =df["wpm"].mean()
acc_media = df["acc"].mean()
best_wpm = df["wpm"].max()
print(f"La wpm media general es {wpm_media:.2f} con una precision del {acc_media:.2f}% de media..")
print(f"Tu wpm mas alta registrada es de {best_wpm} wpm.")