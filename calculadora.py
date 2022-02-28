import pandas as pd


def PV01(lst, tx):  # valor presente
    "Argumentos: lista de listas com uma data e o fluxo e taxa de juros"
    # Convertendo a lista em dataframe
    df = pd.DataFrame(lst, index=["1", "2", "3", "4", "5"],
                      columns=["Ano", "Fluxo de Caixa"])

    print(df)

    # Calculando o valor presente
    df["VP"] = (df["Fluxo de Caixa"])/((1+tx)**df["Ano"])
    print(df)

    # Soma dos valores presentes
    SPV = df["VP"].sum()
    print("Valor Presente: ", SPV)


# Criando uma lista com os dados.
# A lista deve ser composta por sublistas
# contendo a data e o fluxo na data.
lst01 = [[1, 100],
         [2, 100],
         [3, 100],
         [4, 100],
         [5, 100]]

# Definindo a taxa de juros
tx01 = 0.1

PV01(lst01, tx01)
