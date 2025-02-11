%sql
CREATE or Replace TABLE payments (
    transaction_id STRING PRIMARY KEY,
    user_id STRING,
    amount DECIMAL(10,2),
    currency STRING,
    payment_method STRING,
    transaction_status STRING,
    timestamp TIMESTAMP
) USING DELTA;