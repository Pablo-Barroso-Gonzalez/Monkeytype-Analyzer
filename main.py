import pandas as pd

df = pd.read_csv("data/results.csv")

wpm_media =df["wpm"].mean()
print(f"La wpm media general es {wpm_media:.2f}.")



#primeras_filas = df.head()
#ultimas_filas = df.tail()
#nombres_columnas = df.columns
#
#print(f"El df tiene:\nFilas:{filas}\nColumnas:{columnas}")
#print(f"Las primeras filas del df son:\n{primeras_filas} y las ultimas son:\n{ultimas_filas}")
#print("-"*30)
#print(nombres_columnas)#