# pandas- biblioteca que permite interação entre python e excel/planilhas

import pandas as pd

# Importar base de dados
# para ler arquivos em excel: openpyxl

tabela_vendas = pd.read_excel('Vendas.xlsx') 

# Visualizar base de dados / não é obrigatório para o programa rodar, mas é importante para checar se o programa está lendo a base de dados da forma correta

pd.set_option('display.max_columns', None) #pd.set_option(opcao, valor) / None = nesse caso, mostrar o máximo de colunas, nenhuma restrição

print(tabela_vendas)

# Faturamento por loja - agrupar todas as lojas para aparecer 1 vez cada loja e somar o valor final de cada

# Usar:  tabela_vendas[['ID Loja', 'Valor Final']] e tabela_vendas.groupby('ID Loja').sum() // tabela filtrada agrupa todas as lojas e soma o faturamento total por loja =

# 2 colchetes [[]] para filtrar mais de uma coluna, 1 colchete [] para filtrar 1 coluna

faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()

print(faturamento)

# Quantidade de produtos vendidos por loja

quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

print(quantidade)

print('-' * 50)

# Ticket médio por produto em cada loja

# ticket_medio = faturamento['Valor Final'] / quantidade['Quantidade'] ----- dessa forma não é criada uma tabela, é criada uma série de dados

#Quando for para dividir uma coluna por outra:

ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()

print(ticket_medio)

# Enviar email com o relatório