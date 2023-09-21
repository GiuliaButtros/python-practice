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

faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()

print(faturamento)


# Quantidade de produtos vendidos por loja

# Ticket médio por produto em cada loja

# Enviar email com o relatório