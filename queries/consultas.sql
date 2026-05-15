-- =============================================
-- Análise do ENEM 2023 — Consultas SQL
-- Banco: enem.db (SQLite)
-- =============================================

-- 1. Média geral de notas por região
SELECT region,
       ROUND(AVG(mean_score), 2) AS media_geral,
       COUNT(*) AS total_alunos
FROM alunos
GROUP BY region
ORDER BY media_geral DESC;

-- 2. Top 10 estados em Matemática
SELECT state,
       ROUND(AVG(score_math), 2) AS media_math,
       COUNT(*) AS total
FROM alunos
GROUP BY state
ORDER BY media_math DESC
LIMIT 10;

-- 3. Desempenho por tipo de escola em cada região
SELECT region,
       school_type,
       ROUND(AVG(mean_score), 2) AS media,
       COUNT(*) AS total
FROM alunos
WHERE school_type IN ('Public', 'Private')
GROUP BY region, school_type
ORDER BY region, school_type;

-- 4. Impacto do acesso à internet por região
SELECT region,
       has_internet,
       ROUND(AVG(mean_score), 2) AS media,
       COUNT(*) AS total
FROM alunos
GROUP BY region, has_internet
ORDER BY region, has_internet;

-- 5. Renda familiar e desempenho acadêmico
SELECT family_income,
       ROUND(AVG(mean_score), 2) AS media,
       ROUND(AVG(score_math), 2) AS media_math,
       COUNT(*) AS total
FROM alunos
GROUP BY family_income
ORDER BY media DESC;