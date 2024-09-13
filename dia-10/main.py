from IPython.display import display
import pandas as pd
import numpy as np

dados = {"Nomes": ['Ian','James','Tiao','Ana', 'Carlos', 'Beatriz', 'David', 'Fernanda'], "Departamento": ['TI','Suporte','Financeiro','TI', 'RH', 'TI', 'Marketing', 'TI'], "Salário": [1300,1500,1900,5000, 4500, 5500, 4000, 6000]}

df = pd.DataFrame(dados)

print("Qual o departamento que deseja filtrar?")
dep = input("TI - Suporte - Financeiro - Marketing - RH ")

if(dep == "TI" or dep == "Suporte" or dep == "Financeiro" or dep == "Marketing" or dep == "RH"):
    df_Dep  = df[df['Departamento'] == dep]
    media_sal_ti = np.mean(df_Dep["Salário"])
    print(f"A média salarial do departamento de {dep} é: {media_sal_ti}")

    #display(df_Dep)

else:
    print("Departamento incorreto ou inexistente")
