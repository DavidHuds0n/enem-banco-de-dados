import sqlite3
import os

# Caminho do banco — vai ser criado na raiz do projeto
DB_PATH = 'enem.db'

def criar_banco():
    # Conecta ao banco (cria o arquivo se não existir)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Cria a tabela principal
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id                     INTEGER PRIMARY KEY AUTOINCREMENT,
            age                    INTEGER,
            genre                  TEXT,
            race                   TEXT,
            school_type            TEXT,
            state                  TEXT,
            region                 TEXT,
            score_natural          REAL,
            score_human            REAL,
            score_languages        REAL,
            score_math             REAL,
            score_essay            REAL,
            mean_score             REAL,
            father_education       TEXT,
            mother_education       TEXT,
            family_income          TEXT,
            has_cell_phone         INTEGER,
            has_computer           INTEGER,
            has_internet           TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print(f"Banco criado com sucesso em: {os.path.abspath(DB_PATH)}")

if __name__ == '__main__':
    criar_banco()