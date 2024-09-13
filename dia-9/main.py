import pandas as pd
import numpy as np

dados = {"Vendas": [10,20,30,10,0,5]}
df = pd.DataFrame(dados)

media = np.mean(df["Vendas"])
mediana = np.median(df["Vendas"])
desvioP = np.std(df["Vendas"], ddof=1)
max = np.max(df["Vendas"])
min = np.min(df["Vendas"])

print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Desvio Padrão: {desvioP}")
print(f"Máximo: {max}")
print(f"Mínimo: {min}")