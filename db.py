import os
from sqlalchemy import create_engine, text

engine = create_engine(os.environ["DATABASE_URL"])


def save_conversion(from_currency, to_currency, amount, result):
    with engine.begin() as conn:
        conn.execute(
            text(
                "INSERT INTO conversions (from_currency, to_currency, amount, result) "
                "VALUES (:from_currency, :to_currency, :amount, :result)"
            ),
            {
                "from_currency": from_currency,
                "to_currency": to_currency,
                "amount": amount,
                "result": result,
            },
        )


def get_history(limit=10):
    with engine.connect() as conn:
        rows = conn.execute(
            text("SELECT * FROM conversions ORDER BY id DESC LIMIT :limit"),
            {"limit": limit},
        )
        return [dict(row._mapping) for row in rows]
