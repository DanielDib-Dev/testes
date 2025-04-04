-- Cria o banco de dados
CREATE DATABASE IF NOT EXISTS ans_dados;
USE ans_dados;

-- Criação da tabela
CREATE TABLE demonstracoes_contabeis (
    data_ref DATE,
    reg_ans INT,
    cd_conta_contabil VARCHAR(50),
    descricao VARCHAR(255),
    vl_saldo_inicial DECIMAL(20, 2),
    vl_saldo_final DECIMAL(20, 2)
);