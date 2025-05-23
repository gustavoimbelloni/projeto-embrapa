CREATE TABLE IF NOT EXISTS producao (
    id SERIAL PRIMARY KEY,
    ano INTEGER,
    produto TEXT,
    quantidade TEXT,
    parent_id INTEGER REFERENCES producao(id)
);