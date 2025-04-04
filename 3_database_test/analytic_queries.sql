-- Top 10 operadoras com maiores despesas no ÚLTIMO TRIMESTRE disponível
SET @ano := (SELECT MAX(YEAR(data_ref)) FROM demonstracoes_contabeis);
SET @trimestre := (
  SELECT MAX(QUARTER(data_ref)) 
  FROM demonstracoes_contabeis 
  WHERE YEAR(data_ref) = @ano
);

SELECT 
    o.razao_social,
    SUM(d.vl_saldo_final) AS total_despesas,
    @ano AS ano,
    @trimestre AS trimestre
FROM demonstracoes_contabeis d
JOIN operadoras o ON d.reg_ans = o.registro_ans
WHERE d.descricao LIKE '%EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE%'
  AND YEAR(d.data_ref) = @ano
  AND QUARTER(d.data_ref) = @trimestre
GROUP BY o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;

-- Top 10 operadoras com maiores despesas no ÚLTIMO ANO disponível
SET @ano := (SELECT MAX(YEAR(data_ref)) FROM demonstracoes_contabeis);

SELECT 
    o.razao_social,
    SUM(d.vl_saldo_final) AS total_despesas,
    @ano AS ano
FROM demonstracoes_contabeis d
JOIN operadoras o ON d.reg_ans = o.registro_ans
WHERE d.descricao LIKE '%EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE%'
  AND YEAR(d.data_ref) = @ano
GROUP BY o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;