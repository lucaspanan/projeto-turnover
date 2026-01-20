import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel(r"C:\projeto_turnover\turnover_tratado.xlsx")

print(df.head())
print(df.shape)

#calcular a media com (mean)
#como a media vem em formato decimal multiplique por 100 para transformar em porcentagem
tornover_geral = df["Turnover Flag"].mean()*100
print(f"o tornover geral : {tornover_geral:.2f}%")

#calculando o turnover por departamento
tornover_dept= (df.groupby("Department")["Turnover Flag"].mean().sort_values(ascending=False)).mul(100).round(2)

print(tornover_dept)


#criando grafico
tornover_dept.plot(kind="bar")

#Define o título do gráfico
plt.title("turnover por departamento")

#Nomeia o eixo vertical (Y)
#Indica que os valores são porcentagem
plt.ylabel("porcentual (%)")

#Nomeia o eixo horizontal (X)
#Mostra que cada barra corresponde a um departamento
plt.xlabel("Department")

#Ajusta automaticamente o layout
#Evita que textos e rótulos fiquem cortados ou sobrepostos
plt.tight_layout()

#Exibe o gráfico na tela
plt.show()