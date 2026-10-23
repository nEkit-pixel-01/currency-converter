CREATE TABLE conversions (
    id SERIAL PRIMARY KEY,
    from_currency VARCHAR(10),
    to_currency VARCHAR(10),
    amount NUMERIC,
    result NUMERIC,
    created_at TIMESTAMP DEFAULT NOW()
);
