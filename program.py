import pandas as pd

# exibindo planilha no console #
planilha = pd.read_excel("pessoas.xlsx")
# print(planilha) -> teste

# quantidade de linhas no excel - 0 a X #
qtd_linhas = planilha['Nome'].count()
# print(qtd_linhas) -> teste

# input #
id = int(input('Digite o ID: '))
nome = input('Digite o Nome: ')
idade = int(input('Digite a Idade: '))
peso = float(input('Digite o Peso: '))

# ----------------------------------------------------
planilha['ID'].append(id)
planilha['Nome'].append(nome)
planilha['Idade'].append(idade)
planilha['Peso'].append(peso)

# or #
#  localizar quantidade da linha na coluna 'X' -> 'ID' - 'Nome' - 'Idade'.. #
# -> #

# planilha.loc[qtd_linhas+1, 'ID'] = id
# planilha.loc[qtd_linhas+1, 'Nome'] = nome
# planilha.loc[qtd_linhas+1, 'Idade'] = idade
# planilha.loc[qtd_linhas+1, 'Peso'] = peso
# ----------------------------------------------------

# mandar para excel #
planilha.to_excel("pessoas.xlsx" , index=False)