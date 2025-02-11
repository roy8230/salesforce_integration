%sql
-- Create the table
CREATE OR REPLACE TABLE payments (
    transaction_id STRING,
    user_id STRING,
    amount DECIMAL(10,2),
    currency STRING,
    payment_method STRING,
    transaction_status STRING,
    timestamp TIMESTAMP
) USING DELTA;

-- Insert data into the table
%sql
INSERT INTO payments (transaction_id, user_id, amount, currency, payment_method, transaction_status, timestamp) 
VALUES ('T000001', '003GB0000459U9YYAU', 100.00, 'USD', 'credit_card', 'completed', '2022-01-01 12:00:00');
%sql
INSERT INTO payments (transaction_id, user_id, amount, currency, payment_method, transaction_status, timestamp) 
VALUES ('T000002', '003GB0000459U9jYAE', 200.00, 'USD', 'debit_card', 'pending', '2022-01-02 13:00:00');

%sql
INSERT INTO payments (transaction_id, user_id, amount, currency, payment_method, transaction_status, timestamp) 
VALUES ('T000003', '003GB0000459U9SYAU', 300.00, 'USD', 'paypal', 'failed', '2022-01-03 14:00:00');

%sql
INSERT INTO payments (transaction_id, user_id, amount, currency, payment_method, transaction_status, timestamp) 
VALUES ('T000004', '003GB0000459U9gYAE', 400.00, 'USD', 'credit_card', 'completed', '2022-01-04 15:00:00');

%sql
INSERT INTO payments (transaction_id, user_id, amount, currency, payment_method, transaction_status, timestamp) 
VALUES ('T000005', '003GB0000459U9oYAE', 500.00, 'USD', 'debit_card', 'completed', '2022-01-05 16:00:00');

%sql
select * from payments;



