import pandas as pd

df = pd.read_csv("data/results.csv")

primeras_filas = df.head()
ultimas_filas = df.tail()
filas, columas = df.shape

print(f"El df tiene:\nFilas:{filas}\nColumnas:{columas}")
print(f"Las primeras filas del df son:\n{primeras_filas} y las ultimas son:\n{ultimas_filas}")