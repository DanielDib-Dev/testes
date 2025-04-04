LOAD DATA LOCAL INFILE 'C:/Users/dan-d/Documents/GitHub/testes/3_database_test/csv_files/Relatorio_cadop.csv'
INTO TABLE operadoras
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(registro_ans, cnpj, razao_social, nome_fantasia, modalidade,
logradouro, numero, complemento, bairro, cidade, uf, cep, ddd,
telefone, fax, endereco_eletronico, representante, cargo_representante,
@regiao, @data)
SET
    regiao_de_comercializacao = NULLIF(@regiao, ''),
    data_registro_ans = STR_TO_DATE(@data, '%Y-%m-%d');