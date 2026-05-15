# ENEM 2023 — Banco de Dados SQL

Projeto de estruturação e consulta dos microdados do ENEM 2023 em banco de dados relacional, utilizando SQLite e Python.

## 🎯 Objetivo

Migrar os dados do ENEM 2023 (127.574 registros) de um arquivo CSV para um banco de dados relacional, e demonstrar o uso de SQL para análise de dados educacionais.

## 📂 Fonte de Dados

Dataset **Student Performance — ENEM 2023** disponível no Kaggle:  
[Kaggle - Student Performance (ENEM 2023)](https://www.kaggle.com/datasets/jpamcb/student-performance/data)

## 🗃️ Estrutura do Banco

Tabela `alunos` com 127.574 registros e 19 colunas:

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| id | INTEGER | Chave primária |
| age | INTEGER | Idade |
| genre | TEXT | Gênero |
| race | TEXT | Raça/Etnia |
| school_type | TEXT | Tipo de escola |
| state | TEXT | Estado |
| region | TEXT | Região |
| score_natural | REAL | Nota em Ciências da Natureza |
| score_human | REAL | Nota em Ciências Humanas |
| score_languages | REAL | Nota em Linguagens |
| score_math | REAL | Nota em Matemática |
| score_essay | REAL | Nota na Redação |
| mean_score | REAL | Nota média |
| father_education | TEXT | Escolaridade do pai |
| mother_education | TEXT | Escolaridade da mãe |
| family_income | TEXT | Renda familiar |
| has_cell_phone | INTEGER | Possui celular |
| has_computer | INTEGER | Possui computador |
| has_internet | TEXT | Possui internet em casa |

## 📊 Consultas Implementadas

1. Média geral de notas por região
2. Top 10 estados em Matemática
3. Desempenho por tipo de escola em cada região
4. Impacto do acesso à internet por região
5. Renda familiar e desempenho acadêmico

## 🔍 Principais Achados

- **Minas Gerais** lidera em Matemática com média de 597 pontos
- Escolas privadas superam públicas em ~100 pontos em todas as regiões
- Acesso à internet está associado a até 47 pontos a mais na nota média
- Diferença de 186 pontos entre a maior e menor faixa de renda

## 🛠️ Tecnologias

- Python 3.12+
- SQLite3 (built-in)
- Pandas
- SQLAlchemy

## ▶️ Como Rodar

```bash
# 1. Clone o repositório
git clone https://github.com/DavidHuds0n/enem-banco-de-dados.git
cd enem-banco-de-dados

# 2. Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Baixe o dataset e coloque em data/ENEM_2023.csv
# Link: https://www.kaggle.com/datasets/jpamcb/student-performance

# 5. Execute os scripts em ordem
python scripts/01_criar_banco.py
python scripts/02_inserir_dados.py
python scripts/03_consultas.py
```

## 📁 Estrutura do Repositório
```
enem-banco-de-dados/
├── data/           # Dataset (não incluído — ver fonte acima)
├── scripts/        # Scripts Python
│   ├── 01_criar_banco.py
│   ├── 02_inserir_dados.py
│   └── 03_consultas.py
├── queries/
│   └── consultas.sql
├── requirements.txt
└── README.md
```

---
Desenvolvido por [David Hudson](https://github.com/DavidHuds0n)