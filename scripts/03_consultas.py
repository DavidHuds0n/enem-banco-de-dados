import sqlite3
import pandas as pd

DB_PATH = 'enem.db'

def consultar(query, descricao):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(query, conn)
    conn.close()
    print(f"\n{'='*50}")
    print(f"{descricao}")
    print('='*50)
    print(df.to_string(index=False))

# 1. Média de notas por região
consultar("""
    SELECT region,
           ROUND(AVG(mean_score), 2) as media_geral,
           COUNT(*) as total_alunos
    FROM alunos
    GROUP BY region
    ORDER BY media_geral DESC
""", "1. Média geral por região")

# 2. Top 10 estados em Matemática
consultar("""
    SELECT state,
           ROUND(AVG(score_math), 2) as media_math,
           COUNT(*) as total
    FROM alunos
    GROUP BY state
    ORDER BY media_math DESC
    LIMIT 10
""", "2. Top 10 estados em Matemática")

# 3. Pública vs Privada por região
consultar("""
    SELECT region,
           school_type,
           ROUND(AVG(mean_score), 2) as media,
           COUNT(*) as total
    FROM alunos
    WHERE school_type IN ('Public', 'Private')
    GROUP BY region, school_type
    ORDER BY region, school_type
""", "3. Pública vs Privada por região")

# 4. Impacto da internet por região
consultar("""
    SELECT region,
           has_internet,
           ROUND(AVG(mean_score), 2) as media,
           COUNT(*) as total
    FROM alunos
    GROUP BY region, has_internet
    ORDER BY region, has_internet
""", "4. Impacto da internet por região")

# 5. Renda e desempenho
consultar("""
    SELECT family_income,
           ROUND(AVG(mean_score), 2) as media,
           ROUND(AVG(score_math), 2) as media_math,
           COUNT(*) as total
    FROM alunos
    GROUP BY family_income
    ORDER BY media DESC
""", "5. Renda familiar e desempenho")