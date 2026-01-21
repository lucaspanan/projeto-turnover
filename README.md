 Análise de Turnover de Funcionários
***Visão Geral***

Este projeto tem como objetivo analisar a taxa de turnover de funcionários, identificando padrões de desligamento e áreas com maior rotatividade.
A análise foi desenvolvida utilizando Excel, Python e Power BI, simulando um cenário real de análise de dados aplicada à área de Recursos Humanos.

*** Objetivo do Projeto***

Calcular a taxa de turnover geral da empresa
Identificar departamentos e perfis com maior rotatividade
Gerar insights que possam apoiar decisões estratégicas de RH

***Base de Dados***

Foi utilizada uma base de dados pública disponibilizada no Kaggle:
IBM HR Analytics – Employee Attrition & Performance

📌 A base contém informações demográficas, profissionais e comportamentais dos colaboradores.
📌 Os dados foram utilizados exclusivamente para fins educacionais.

***🛠️ Ferramentas Utilizadas***

Excel → Tratamento de dados e criação de regras de negócio
Python (pandas, matplotlib) → Análise exploratória e cálculos
Power BI → Visualização dos indicadores e criação do dashboard

***🧹 Tratamento dos Dados (Excel)***

No Excel, foram realizadas as seguintes etapas:
Conferência de valores nulos e duplicados
Criação de colunas de apoio para análise:
Status do Funcionário (Ativo / Desligado)
Turnover Flag (1 = desligado, 0 = ativo)
Faixa Etária
Faixa de Tempo de Casa
Estruturação da base como tabela, facilitando a integração com Python e Power BI

***🧮 Cálculo da Taxa de Turnover Geral***

A taxa de turnover foi calculada a partir da média da variável binária Turnover Flag, onde:
1 representa funcionários desligados
0 representa funcionários ativos
O resultado foi multiplicado por 100 para obtenção do percentual de turnover da empresa.

***📊 Turnover por Departamento***

A taxa de turnover por departamento foi calculada utilizando a média da variável Turnover Flag, agrupada por área.
Os valores foram convertidos em percentual, arredondados para duas casas decimais e ordenados de forma decrescente, facilitando a identificação dos departamentos com maior rotatividade.

***📈 Análise Exploratória (Python)***

Com Python, foi realizada:
Leitura da base tratada em Excel
Cálculo do turnover geral
Cálculo do turnover por departamento
Criação de gráfico de barras para visualização da rotatividade por área

***📊 Visualização dos Dados (Power BI)***

No Power BI, foi desenvolvido um dashboard interativo, contendo:

KPIs
Total de Funcionários
Total de Desligados
Taxa de Turnover (%)
Visuaiss
Turnover por Departamento
Turnover por Cargo
Distribuição de Funcionários Ativos x Desligados
Turnover por Tempo de Casa
Filtros
Departamento
Cargo
Gênero
Hora Extra (OverTime)

***💡 Principais Insights***

O departamento de Sales apresenta o maior índice de turnover em comparação às demais áreas
Funcionários com menos tempo de casa concentram a maior parte dos desligamentos
Colaboradores que realizam hora extra demonstram maior propensão ao turnover
Esses padrões podem indicar desafios relacionados a metas, carga de trabalho ou processos de onboarding.
