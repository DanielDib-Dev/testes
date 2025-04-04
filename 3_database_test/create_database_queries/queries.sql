-- Cria o banco de dados
CREATE DATABASE IF NOT EXISTS ans_dados;
USE ans_dados;

-- Criação das tabelas
CREATE TABLE demonstracoes_contabeis (
    data_ref DATE,
    reg_ans INT,
    cd_conta_contabil VARCHAR(50),
    descricao VARCHAR(255),
    vl_saldo_inicial DECIMAL(20, 2),
    vl_saldo_final DECIMAL(20, 2)
);

CREATE TABLE IF NOT EXISTS operadoras (
    registro_ans INT PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(5),
    telefone VARCHAR(15),
    fax VARCHAR(15),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(100),
    regiao_de_comercializacao TINYINT,
    data_registro_ans DATE
);