SELECT * FROM conversions ORDER BY id DESC LIMIT 10;


SELECT from_currency, COUNT(*) FROM conversions GROUP BY from_currency;


SELECT from_currency, SUM(amount) FROM conversions GROUP BY from_currency;

SELECT from_currency, to_currency
FROM conversions
GROUP BY from_currency, to_currency
ORDER BY COUNT(*) DESC
LIMIT 1;
