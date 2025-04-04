# Teste de Nivelamento

Este repositório contém as soluções desenvolvidas para um teste de nivelamento.

## Estrutura do Projeto

O projeto está organizado nos seguintes módulos:

1. **Web Scraping**
   - Acesso ao site da ANS
   - Download dos Anexos I e II
   - Compactação dos arquivos
   - **Scripts**: `1_web_scrapping_test/anexo_scraper.py`

2. **Transformação de Dados**
   - Extração de dados da Tabela de Procedimentos e Eventos de Saúde do PDF do Anexo I
   - Conversão dos dados para CSV
   - **Scripts**: `2_data_transformation_test/pdf_to_csv.py`

3. **Banco de Dados**
   - Criação e manipulação de tabelas no banco de dados
   - Carregamento de dados a partir de arquivos CSV
   - **Scripts**: 
     - `3_database_test/create_database_queries/queries.sql`
     - `3_database_test/load_health_plan_operators.sql`
     - `3_database_test/load_last_2_years_query.sql`
     - `3_database_test/analytic_queries.sql`

4. **API e Interface Web**
   - **Observação**: Este módulo não foi concluído devido à falta de conhecimento técnico em Vue.js.

## Requisitos

- Python 3.x
- Bibliotecas: `requests`, `beautifulsoup4`, `pandas`, `tabula-py`, `zipfile`
- MySQL Server para manipulação de dados

## Licença

Este projeto é confidencial e não deve ser divulgado sem autorização expressa.
