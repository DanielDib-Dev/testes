-- 1º Trimestre 2023
LOAD DATA LOCAL INFILE 'C:/Users/dan-d/Documents/GitHub/testes/3_database_test/csv_files/last_2_years/1T2023.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    data_ref = STR_TO_DATE(@data, '%Y-%m-%d'),
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

-- 2º Trimestre 2023
LOAD DATA LOCAL INFILE 'C:/Users/dan-d/Documents/GitHub/testes/3_database_test/csv_files/last_2_years/2T2023.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    data_ref = STR_TO_DATE(@data, '%Y-%m-%d'),
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

-- 3º Trimestre 2023
LOAD DATA LOCAL INFILE 'C:/Users/dan-d/Documents/GitHub/testes/3_database_test/csv_files/last_2_years/3T2023.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    data_ref = STR_TO_DATE(@data, '%Y-%m-%d'),
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

-- 4º Trimestre 2023
LOAD DATA LOCAL INFILE 'C:/Users/dan-d/Documents/GitHub/testes/3_database_test/csv_files/last_2_years/4T2023.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    data_ref = STR_TO_DATE(@data, '%d/%m/%Y'),
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');
    
-- 1º Trimestre 2024
LOAD DATA LOCAL INFILE 'C:/Users/dan-d/Documents/GitHub/testes/3_database_test/csv_files/last_2_years/1T2024.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    data_ref = STR_TO_DATE(@data, '%Y-%m-%d'),
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

-- 2º Trimestre 2024
LOAD DATA LOCAL INFILE 'C:/Users/dan-d/Documents/GitHub/testes/3_database_test/csv_files/last_2_years/2T2024.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    data_ref = STR_TO_DATE(@data, '%Y-%m-%d'),
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

-- 3º Trimestre 2024
LOAD DATA LOCAL INFILE 'C:/Users/dan-d/Documents/GitHub/testes/3_database_test/csv_files/last_2_years/3T2024.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    data_ref = STR_TO_DATE(@data, '%Y-%m-%d'),
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

-- 4º Trimestre 2024
LOAD DATA LOCAL INFILE 'C:/Users/dan-d/Documents/GitHub/testes/3_database_test/csv_files/last_2_years/4T2024.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    data_ref = STR_TO_DATE(@data, '%Y-%m-%d'),
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');