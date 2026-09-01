import pandas as pd

df = pd.read_csv("data/results.csv")

wpm_media =df["wpm"].mean()
acc_media = df["acc"].mean()
best_wpm = df["wpm"].max()
mejor_test = df[df["wpm"] == best_wpm]

print(f"La wpm media general es {wpm_media:.2f} con una precision del {acc_media:.2f}% de media..")
print(f"""Tu wpm mas alta registrada es de {best_wpm} wpm con:
acc   → {mejor_test["acc"].iloc[0]}
mode  → {mejor_test["mode"].iloc[0]}
mode2 → {mejor_test["mode2"].iloc[0]}
""")