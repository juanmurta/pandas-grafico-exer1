import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter

caminho_padrao = r'E:\Cursos\Estudos\Impressionador\PowerBi'

# importando os arquivos
vendas_df = pd.read_csv(os.path.join(caminho_padrao, r'Contoso - Vendas - 2017.csv'), sep=';')
produtos_df = pd.read_csv(os.path.join(caminho_padrao, r'Contoso - Cadastro Produtos.csv'), sep=';', encoding='ISO-8859-1')
lojas_df = pd.read_csv(os.path.join(caminho_padrao, r'Contoso - Lojas.csv'), sep=';', encoding='ISO-8859-1')
clientes_df = pd.read_csv(os.path.join(caminho_padrao, r'Contoso - Clientes.csv'), sep=';', encoding='ISO-8859-1')


# selecionando as colunas que queremos
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]


# mesclando e renomeando os dataframes
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente').rename(columns={'E-mail': 'E-mail do Cliente'})


# filtrando as lojas
dataset = vendas_df
tres_lojas_df = dataset[dataset['ID Loja'].isin([86, 306, 172])]
tres_lojas_df['Data da Venda'] = pd.to_datetime(tres_lojas_df['Data da Venda'], format='%d/%m/%Y')


# mostrando gráficos python matplotlib
tres_lojas_df.plot(x='Data da Venda', y='Quantidade Vendida', figsize=(15, 5))
plt.show()


# mostrando gráficos no seaborn
sns.set_theme(style='darkgrid')
fig, ax = plt.subplots(figsize=(15, 5))

# editando eixo
ax.xaxis.set_major_locator(plt.MaxNLocator(12))
ax.xaxis.set_major_formatter(DateFormatter('%m'))

# plotando grafico
sns.lineplot(x='Data da Venda', y='Quantidade Vendida', hue='Nome da Loja', data=tres_lojas_df, ax=ax)
plt.show()
