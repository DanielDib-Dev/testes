# Configurações Realizadas

Foi preciso fazer algumas alterações para que tudo pudesse funcionar corretamente. Abaixo estão listadas todas as alterações realizadas:

## Configurações do MySQL Server

Alterei o arquivo `my.ini` do MySQL Server para que pudesse utilizar o `LOAD DATA LOCAL`:

```ini
[client]
loose-local-infile=1

[mysqld]
secure-file-priv=""
local_infile=1
```

## Formato de Data

Além disso, notei que um dos CSVs possuía um formato de data diferente, e isso foi adaptado na query.

# Rodar Query

Para utilizar a query é necessário mudar o diretório de acordo com onde você clonou o repositório.

# Erro

Consegui criar com sucesso o banco de dados e as tabelas, porém cometi algum erro na hora de dar os loads dos arquivos csv, gerando valores errados nas queries analíticas.