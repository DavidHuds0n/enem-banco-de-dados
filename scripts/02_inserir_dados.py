import sqlite3
import pandas as pd

DB_PATH = 'enem.db'
CSV_PATH = 'data/ENEM_2023.csv'

def inserir_dados():
    print("Carregando CSV...")
    df = pd.read_csv(CSV_PATH)

    # Renomeia as colunas para bater com a tabela
    df.columns = [
        'age', 'genre', 'race', 'school_type', 'state', 'region',
        'score_natural', 'score_human', 'score_languages', 'score_math',
        'score_essay', 'mean_score', 'father_education', 'mother_education',
        'family_income', 'has_cell_phone', 'has_computer', 'has_internet'
    ]

    print(f"Inserindo {len(df)} registros no banco...")
    conn = sqlite3.connect(DB_PATH)

    # if_exists='append' adiciona os dados sem apagar a tabela
    df.to_sql('alunos', conn, if_exists='append', index=False)

    conn.close()
    print("Dados inseridos com sucesso!")

    # Verifica se deu certo
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM alunos")
    total = cursor.fetchone()[0]
    conn.close()
    print(f"Total de registros no banco: {total}")

if __name__ == '__main__':
    inserir_dados()