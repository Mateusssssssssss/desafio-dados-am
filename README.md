# Descrição dos dados obtidos no kaggle
O crescimento dos supermercados na maioria das cidades populosas está aumentando e as competições de mercado também são altas. O conjunto de dados é uma das vendas históricas da empresa de supermercados que registrou em 3 filiais diferentes por 3 meses de dados. 


# Criação das tabelas no PostgreSQL:
```sql
CREATE TABLE supermarket_sales.sales (
    invoice_id VARCHAR(20) PRIMARY KEY,
    branch VARCHAR(10) NOT NULL,
    city VARCHAR(50) NOT NULL,
    customer_type VARCHAR(20) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    product_line VARCHAR(100) NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    quantity INT NOT NULL,
    tax_5_percent DECIMAL(10,2) NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL,
    payment VARCHAR(20) NOT NULL,
    cogs DECIMAL(10,2) NOT NULL,
    gross_margin_percentage DECIMAL(10,4) NOT NULL,
    gross_income DECIMAL(10,2) NOT NULL,
    rating DECIMAL(3,1)
);
```
# Para integração dos dados foi usado comando direto no PSQL Tool

 \copy supermarket.dados FROM 'C:caminho/supermarket.csv' DELIMITER ',' CSV HEADER;

# Leitura dos dados Através da Bigquery da GCP:

O arquivo foi importado para o BigQuery para análise dos dados. Para isso, selecionei a opção 'Adicionar' e depois 'Arquivo local', escolhi o arquivo desejado e nomeei o conjunto de dados como 'case_estagio' (multiregional - US). Após isso, criei o conjunto de dados e nomeei a tabela como 'sales', selecionando a opção de detectar o esquema automaticamente e, em seguida, criei a tabela.

# Codigos Usados:
 Para visualizar toda a tabela:
SELECT * FROM `eloquent-life-440311-t4.case_estagio.sales` LIMIT 1000

Para verificar valores nulos: 
```sql
SELECT
    COUNT(CASE WHEN `invoice_id` IS NULL THEN 1 END) AS invoice_id_null_count,
    COUNT(CASE WHEN `branch` IS NULL THEN 1 END) AS branch_null_count,
    COUNT(CASE WHEN `city` IS NULL THEN 1 END) AS city_null_count,
    COUNT(CASE WHEN `customer_type` IS NULL THEN 1 END) AS customer_type_null_count,
    COUNT(CASE WHEN `gender` IS NULL THEN 1 END) AS gender_null_count,
    COUNT(CASE WHEN `product_line` IS NULL THEN 1 END) AS product_line_null_count,
    COUNT(CASE WHEN `unit_price` IS NULL THEN 1 END) AS unit_price_null_count,
    COUNT(CASE WHEN `quantity` IS NULL THEN 1 END) AS quantity_null_count,
    COUNT(CASE WHEN `tax_5_percent` IS NULL THEN 1 END) AS tax_5_percent_null_count,
    COUNT(CASE WHEN `total` IS NULL THEN 1 END) AS total_null_count,
    COUNT(CASE WHEN `date` IS NULL THEN 1 END) AS date_null_count,
    COUNT(CASE WHEN `time` IS NULL THEN 1 END) AS time_null_count,
    COUNT(CASE WHEN `payment` IS NULL THEN 1 END) AS payment_null_count,
    COUNT(CASE WHEN `cogs` IS NULL THEN 1 END) AS cogs_null_count,
    COUNT(CASE WHEN `gross_margin_percentage` IS NULL THEN 1 END) AS gross_margin_percentage_null_count,
    COUNT(CASE WHEN `gross_income` IS NULL THEN 1 END) AS gross_income_null_count,
    COUNT(CASE WHEN `rating` IS NULL THEN 1 END) AS rating_null_count
FROM `eloquent-life-440311-t4.case_estagio.sales`;
```
# Filtro feito para colunas que seriam usadas:
# consulta salva como dataset formato csv:
```sql
SELECT 
  Payment,
  Total,
  Quantity,
  Unit_price,
  Customer_type,
  Product_line,
  Gender,
  City
FROM `eloquent-life-440311-t4.case_estagio.sales`
```

[Arquivo antes do Filtro](data/supermarket_sales.csv)
[Arquivo depois do filtro](data/supermarket_filter.csv)


# Para verificar media por linha de produtos:
```sql
SELECT Product_line, AVG(total) AS media_total
FROM `eloquent-life-440311-t4.case_estagio.sales`
GROUP BY product_line;
```

# Valor total de vendas por filial: 
```sql
SELECT branch, SUM(total) AS total_vendas
FROM `eloquent-life-440311-t4.case_estagio.sales`
GROUP BY branch;
```
![Valor total de vendas por filial](<image/valor de vendas por filial.png>)

# Valor total de vendas por linha de produto: 
```sql
SELECT product_line, SUM(total) AS total_vendas
FROM `eloquent-life-440311-t4.case_estagio.sales`
GROUP BY product_line;
```
![Valor total de vendas por linha de produto](<image/valor de vendas por linha de produtos.png>)

# Quantidade total vendida por linha de produto:
```sql
SELECT product_line, SUM(quantity) AS total_quantidade
FROM `eloquent-life-440311-t4.case_estagio.sales`
GROUP BY product_line;
```
![Quantidade total vendida por linha de produto](<image/Quantidades de itens vendidos por linha de produtos.png>)


# Valor de Vendas por cidade
```sql
SELECT city, SUM(total) AS total_vendas
FROM `eloquent-life-440311-t4.case_estagio.sales`
GROUP BY city;
```

![Valor de Vendas por Cidade](<image/valor de vendas por cidade.png>)


# Vendas por metodo de pagamento
```sql
SELECT payment, SUM(total) AS total_vendas
FROM `eloquent-life-440311-t4.case_estagio.sales`
GROUP BY payment;
```
![Vendas por Metodo de Pagamento](<image/Metodos de pagamentos usados.png>)

# Valor de vendas por produto e genero:
```sql 
SELECT product_line, gender, SUM(total) AS total_vendas
FROM `eloquent-life-440311-t4.case_estagio.sales`
GROUP BY product_line, gender;
```
![Valor e Quantidade de vendas Masculinas](<image/comparação entre valor e quantidade por homens.png>)
![Valor e Quantidade de vendas Femininas](<image/comparação entre valor e quantidade por mulheres.png>)

# Comparação de vendas entre homens e mulheres

SELECT product_line, gender, SUM(total) AS total_vendas
```sql
    FROM eloquent-life-440311-t4.case_estagio.sales
    WHERE gender IN ('Male', 'Female')
    GROUP BY product_line, gender
    ORDER BY gender;
```

![Valor de vendas por genero](<image/valor de vendas por sexo.png>)
![Comparação entre Homens e Mulheres](<image/comparação de linhas de produtos vendidos entre mulher e homem.png>)


# Usando Power Bi
Ao abrir o dataset no Power BI, as colunas numéricas foram interpretadas como texto. Para corrigir isso, utilizei o Power Query para converter os dados de texto em valores numéricos decimais.

[Link do Relatorio no Power Bi](https://app.powerbi.com/links/s7DMTmb9Jb?ctid=da49a844-e2e3-40af-86a6-c3819d704f49&pbi_source=linkShare&bookmarkGuid=618e5582-8146-4942-a83f-902e80c63439)


# Arquivo extra
[Análise Explorátoria de Dados (EDA)](archives/supermarket.py)
[Readme da analise exploratoria usando Bibliotecas Python](archives/README)