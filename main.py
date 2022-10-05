import pandas as pd
import plotly.express as px

#Configurar a exibição da tabela no run do pandas
pd.set_option("display.max_columns", None)

#Mostrar nossa base de dados e tirar a coluna que está atrapalhando Unnamed: 0
tabela = pd.read_csv("telecom_users.csv")
tabela = tabela.drop("Unnamed: 0", axis=1)
print(tabela.info())

#Trocar o tipo dos dados que estão sendo salvo na coluna total gasto de texto, para numero
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

#Apagar as colunas inteiramente vazias
tabela = tabela.dropna(how="all", axis=1)

#Apagar linhas com conteudo que estejam em vazio
tabela = tabela.dropna(how="any", axis=0)

#Contar a quantidade de pessoas que cancelaram e não cancelaram
print(tabela["Churn"].value_counts())

#Normalizar em porcentagem o resultado de cima
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

#Para cada coluna na tabela rodar esse codigo:

for coluna in tabela.columns:
    #Criando um grafico
    grafico = px.histogram(tabela, x=coluna, color="Churn")

    #Exibir o grafico
    grafico.show()