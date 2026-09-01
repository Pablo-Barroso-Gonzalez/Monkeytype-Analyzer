import pandas as pd

df = pd.read_csv("data/results.csv")

wpm_media =df["wpm"].mean()
acc_media = df["acc"].mean()
best_wpm = df["wpm"].max()
print(f"La wpm media general es {wpm_media:.2f} con una precision del {acc_media:.2f}% de media..")
print(f"Tu wpm mas alta registrada es de {best_wpm} wpm.")

#for valor in df["wpm"]:
#    if valor > best_value:
#        best_value = valor
#print(f"El valor mas alto de wpm que has logrado es {best_value} wpm.")

#primeras_filas = df.head()
#ultimas_filas = df.tail()
#nombres_columnas = df.columns
#
#print(f"El df tiene:\nFilas:{filas}\nColumnas:{columnas}")
#print(f"Las primeras filas del df son:\n{primeras_filas} y las ultimas son:\n{ultimas_filas}")
#print("-"*30)
#print(nombres_columnas)#