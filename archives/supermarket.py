import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
#Ler o csv
dados = pd.read_csv('data\supermarket_sales.csv')
#Imprimi as 5 primeiras linhas
print(dados.head())
#Verificar se há valores nulos
dados_null = dados.isnull().sum()
print(dados_null)
#Verificar se a há dados duplicados
dados_dup = dados.duplicated().sum()
print(dados_dup)
#Descrição dos dados
dados_describe = dados.describe()
print(dados_describe)

#Verificar outlier
# Verificado, outliers existentes
sb.boxplot(dados)
plt.show()
#Grafico para identificar outliers na tabela valor
sb.boxplot(dados['Total'])
plt.show()
# outliers com valor acima de 950
out = dados[dados['Total'] >= 950]
print(out)
# Quais linhas de produtos são compativeis com esses outliers
colum = out[['Total','Product line']]
print(colum)

#Media de preço por linha de produtos
media_product = dados.groupby('Product line')['Total'].mean().reset_index()
print(media_product)
# Justificativa para não remover outliers nas vendas:
#Após analisar os dados, percebi que os outliers não são erros, mas sim compras de alto valor, 
# como sofás, geladeiras e bicicletas de corrida, que justificam os valores elevados. 
# O unit price não apresenta anomalias, então não há problema com os preços unitários. 
# Em vez de substituir esses valores pela média, decidi mantê-los, 
# pois refletem transações reais e ajudam a entender o comportamento de compra no mercado, 
# especialmente para produtos de alto custo.



#Agrupa os dados por Filial e retorna o valor total de vendas por filial
# Filial com maior numero de vendas: Filial C porém as outras duas filias mantiveram valor de vendas compativeis
dados_group_branch = dados.groupby('Branch')['Total'].sum().reset_index()
#Grafico gerado usando Seaborn
sb.barplot(dados_group_branch, x='Branch', y='Total', hue='Branch')
# Cria um titulo
plt.title('Valor de vendas por Filial')
# Carrega o grafico
plt.show()
# Agrupa por linhas de produtos e retorna o valor vendido em cada linha de produto
# Produtos da Linha Comidas e Bebidas tivem maior valor de vendas e saude e beleza menores vendas
dados_group_product_line = dados.groupby('Product line')['Total'].sum().reset_index()
# Grafico gerado usando Seaborn
sb.barplot(dados_group_product_line, x='Product line', y='Total', hue='Product line')
# Cria um titulo
plt.title('Valor de vendas por Linhas de Produtos')
# Carrega o grafico
plt.show()
# Agrupa por linha de produtos e retorna quantidade vendidas por linha de produtos
# Maior Quantidade de linha de produto vendidos, foram acessorios eletronicos e 
# menor quantidade de linha vendidas, foram saude e beleza
dados_group_product_line = dados.groupby('Product line')['Quantity'].sum().reset_index()
sb.lineplot(dados_group_product_line, x='Product line', y='Quantity', color='red')
plt.title('Quantidade de Itens Vendidos por Linha de Produtos')
plt.show()

# Agrupa por cidade e retorna a soma do valor de vendas por cidade
#Cidade com maior percuntal de valor vendido foi Naypyitaw, as outras duas duas cidades mantiveram
#percentuais de vendas iguas
dados_group_city = dados.groupby('City')['Total'].sum().reset_index()
# Grafico gerado usando Matplotlib: Grafico de pizza
plt.pie(dados_group_city['Total'], labels=dados_group_city['City'], autopct='%1.1f%%', startangle=90)
# Cria um titulo
plt.title('Porcentagem Valor de Vendas por Cidade')
# Carrega o grafico
plt.show()

# Valor de vendas por cidade
sb.barplot(dados_group_city, x='City', y='Total', hue='City')
plt.title('Valor de vendas por cidade')
plt.show()

# Agrupa por Tipos de pagamentos
# Metodo de pagamento mais usado: Dinheiro, e o menor: Cartão de Credito
dados_group_payment = dados.groupby('Payment')['Quantity'].sum().reset_index()
# Grafico gerado usando Seaborn
sb.barplot(dados_group_payment, x='Payment', y='Quantity', hue='Payment')
# Cria um titulo
plt.title('Metodos de Pagamento Usados')
# Carrega o grafico
plt.show()
# Agrupa por genero e retorna valor de vendas por genero
# Mulheres compraram mais que os homens
dados_group_gender = dados.groupby('Gender')['Total'].sum().reset_index()
# Grafico gerado usando Seaborn
sb.barplot(dados_group_gender, x='Gender', y='Total', hue='Gender')
# Cria um titulo
plt.title('Valor de vendas por Sexo')
# Carrega o grafico
plt.show()

# Filtra dados apenas por mulheres

gender_female = dados[dados['Gender'] == 'Female']
#Agrupa por linhas de produtos e retorna produtos que mais geraram receita por sexo Feminino
#Linha de produtos onde as mulheres mais gastam: comida e bebidas
# e menor linha: Saúde e beleza
dados_group_female_valor = gender_female.groupby('Product line')['Total'].sum().reset_index()
# Linha de produtos com Maior Quantidade de vendas por mulheres: Acessorios de moda
# menor: Saúde e beleza
dados_group_female_quantity = gender_female.groupby('Product line')['Quantity'].sum().reset_index()
# Grafico gerado usando Seabornd
plt.figure()
plt.subplot(2,1,1)
sb.barplot(dados_group_female_valor, x='Product line', y='Total', hue='Product line')
#Tira a descrição do eixo x
plt.xlabel('')
#cria um titulo
plt.title('Linhas de produtos com maior Valor arrecadado entre as mulheres:\nValor R$')

plt.subplot(2,1,2)
sb.barplot(dados_group_female_quantity, x='Product line', y='Quantity', hue='Product line')
#Cria um titulo
plt.title('Linha de produtos com maior Quantidade de vendas entre as mulheres')
# Carrega o grafico
plt.show()
#Filtra dados apenas por Homens
gender_male = dados[dados['Gender'] == 'Male']
#Agrupa por linhas de produtos e retorna produtos que mais geraram receita por sexo Masculino
# Linha de produtos onde os Homens mais gastaram: Saúde e beleza
# e menor linha: comida e bebidas
dados_group_male_valor = gender_male.groupby('Product line')['Total'].sum().reset_index()
# Linha de produtos com Maior Quantidade de vendas por Homens: Saúde e beleza
# menor: Acessorios de moda
dados_group_male_quantity = gender_male.groupby('Product line')['Quantity'].sum().reset_index()
# Grafico gerado usando Seaborn
plt.figure()
plt.subplot(2,1,1)
sb.barplot(dados_group_male_valor, x='Product line', y='Total', hue='Product line')
#Deixar o eixo x sem legenda, para usar colocar um titulo
plt.xlabel('')
#Titulo
plt.title('Linhas de produtos com maior Valor arrecadado entre as homens:\nValor R$')
plt.subplot(2,1,2)
sb.barplot(dados_group_male_quantity, x='Product line', y='Quantity', hue='Product line')
# Cria um titulo
plt.title('Linha de produtos com maior Quantidade de vendas entre as homens')
# Carrega o grafico
plt.show()

# Cria uma figura em branco
plt.figure()
# Plota uma figura
plt.subplot(2,1,1)
# Grafico gerado usando Seaborn
sb.barplot(dados_group_female_valor, x='Product line', y='Total', hue='Product line')
# Cria um titulo
plt.title('Comparação de Linhas de Produtos mais vendidos Mulheres X Homens:\nMulheres')
plt.xlabel('')
# Plota uma figura
plt.subplot(2,1,2)
# Grafico gerado usando Seaborn
sb.barplot(dados_group_male_valor, x='Product line', y='Total', hue='Product line')

# Cria um titulo
plt.title('Homens')
# Carrega o grafico
plt.show()









