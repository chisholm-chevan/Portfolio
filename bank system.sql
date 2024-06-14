USE `banking_system`;
Create Database `Banking_System`;
CREATE TABLE `Account Table` (
Acc_ID INT PRIMARY KEY NOT NULL,
cust_id INT REFERENCES customer (cust_id),
Acct_num INT NOT NULL,
Acct_type varchar(15) NOT NULL,
Acct_srt_date date NOT NULL,
Join_acc_flg char(1) NOT NULL,
Acct_status char(1) NOT NULL
);
select * from `Account Table`;
ALTER TABLE `Account Table`
ADD COLUMN card_type ENUM ('Debit' ,'Credit') DEFAULT 'Debit';

DROP table users;

CREATE TABLE transaction_
(
Tran_id INT PRIMARY KEY,	
Acc_ID INT,
FOREIGN KEY (Acc_ID) REFERENCES `Account Table`(Acc_ID),
tran_type ENUM ('ATM Debit Card WD', 'ATM Credit Card WD', 'Cheque Deposit', 'Cash Deposit'),
tran_amt INT,
tran_date DATE,
last_transaction DATE,
total_transactions_amt INT 
);

SELECT A.Acc_ID, T.tran_type, A.Acct_type, A.Acct_status
From `Account Table` AS A
JOIN transaction_ AS T ON A.Acc_ID = T.Acc_ID;

CREATE TABLE customer(
cust_id INT PRIMARY KEY,
trn_ INT,
title VARCHAR(10) NOT NULL,
F_name VARCHAR(20) NOT NULL,
L_Name VARCHAR(20) NOT NULL,
phone INT NOT NULL, -- Converted to varchar
address VARCHAR(45) NOT NULL,
email VARCHAR(45) NOT NULL,
DOB DATE NOT NULL,
gender VARCHAR(1),
rel_status VARCHAR(2),
cust_status VARCHAR(10), -- Converted to ENUM
comments VARCHAR(30)  -- Converted to ENUM
);
select * from customer;

CREATE TABLE customer_verification(
cust_id INT,
FOREIGN KEY (cust_id) REFERENCES customer(cust_id),
verification_id INT PRIMARY KEY,
status_ VARCHAR(15),
result VARCHAR(10)
);


CREATE TABLE card(
Acc_ID INT,
FOREIGN KEY (Acc_ID) REFERENCES `Account Table`(Acc_ID),
card_num INT NOT NULL,
card_exp_date DATE NOT NULL,
card_type VARCHAR (6)
);

CREATE TABLE Loan(
Loan_id INT PRIMARY KEY,
Acc_ID INT,
FOREIGN KEY (Acc_ID) REFERENCES `Account Table` (Acc_ID),
Loan_amt INT NOT NULL,
Loan_srt_date DATE NOT NULL,
Loan_end_date DATE NOT NULL,
mthly_payment INT NOT NULL,
Loan_bal_remain INT NOT NULL
);
-- QUERIES SECTION ------------------------------------------------------------------------------------------------------------
-- -------------------------------------------------------------------------CUSTOMER QUERIES------------------------------------------------------------------------
ALTER TABLE customer
MODIFY cust_status ENUM ('ACTIVE', 'INACTIVE', 'REJECTED');

ALTER TABLE customer
MODIFY comments ENUM ('Account created successfully', 'BGV FAILED', 'Account creation in progress');

ALTER TABLE customer
MODIFY phone VARCHAR(15);

-- SELECT COUNT(T.total_transactions_amt), C.address, C.cust_id, T.Tran_id
-- FROM customer AS C
-- INNER JOIN transaction_ AS T ON C.cust_id = T.tran_id
-- GROUP BY C.address;

INSERT INTO customer VALUES(00111,131395,"Mr.","Chevan","Chisholm","876-424-2950","Kingston","chev@gmail.com","2000-04-13","M","S","ACTIVE","Account created successfully");
INSERT INTO customer VALUES(00112,131396,"Mr.","Mike","Darnold","876-424-8997","Kingston ","Mike123@gmail.com","2000-05-13","F","M","ACTIVE","Account created successfully");
INSERT INTO customer VALUES(00118,131397,"Ms.","Sarah","Burt","876-424-8889","Kinsgton","sarah123@gmail.com","2000-08-13","M","M","INACTIVE","BGV Failed");
INSERT INTO customer VALUES(00119,131399,"Mr.","Henry","Ford","876-245-0990","Portmore","henry@gmail.com","2010-07-13","F","M","ACTIVE","Account created successfully");
INSERT INTO customer VALUES(00120,131400,"Ms.","Abigale","Williams","876-245-1010","Portmore","abbywill@gmail.com","2000-05-14","F","M","INACTIVE","Account creation in progress");
INSERT INTO customer VALUES(00121,131401,"Ms.","Lisa","Scott","876-245-1010","Portmore","Lscottie@gmail.com","2000-09-23","F","M","ACTIVE","Account created successfully");
INSERT INTO customer VALUES(00122,131402,"Mr.","Troy","Barret","876-245-4455","Kingston","tb@gmail.com","2000-05-21","F","M","ACTIVE","Account created successfully");
INSERT INTO customer VALUES(00123,131403,"Ms.","Dena","Gordon","876-275-8710","Portmore","dgordongmail.com","2000-12-17","F","M","ACTIVE","Account created successfully");

UPDATE customer
SET comments = 'BGV Failed'
WHERE cust_id = 120;

-- -----------------------------------------------------------------ACCOUNT TABLE QUERIES-----------------------------------------------------------------
-- Generate a query to show which customers are qualified for a loan. 
-- These customers have to be with the bank for atleast 24 months
SELECT * FROM `Account Table` 
WHERE (Timestampdiff(year, Acct_srt_date, NOW())) > 2;



WITH C_tran AS (SELECT count(Tran_id) as Num_of_Tran, A.Branch AS Locations FROM `Account Table` AS A 
INNER JOIN transaction_ T
Using (Acc_ID)
INNER JOIN customer C
USING (cust_id) GROUP BY Locations)
SELECT * FROM C_tran HAVING Num_of_Tran <> 0 ;-- (SELECT COUNT(Num_of_tran) FROM C_tran); -- The Query run but is only showing the transaction for kingston, fix it up to show portore and Manchester



ALTER TABLE `Account Table`
MODIFY Acct_status ENUM('ACTIVE', 'INACTIVE', 'DISABLED') DEFAULT 'DISABLED';

INSERT INTO `account table` VALUES (19000,00111,364001,'Debit','2020-01-02','N','ACTIVE','DEBIT');
INSERT INTO `account table` VALUES (19001,00112,364002,'Debit','2021-04-04','N','ACTIVE','DEBIT');
INSERT INTO `account table` VALUES (19002,00119,364003,'Debit','2023-04-06','N','ACTIVE','DEBIT');
INSERT INTO `account table` VALUES (19003,00121,364004,'Debit','2022-05-08','N','ACTIVE','DEBIT');
INSERT INTO `account table` VALUES (19004,00122,364005,'Debit','2021-02-10','N','ACTIVE','DEBIT');
INSERT INTO `account table` VALUES (19005,00123,364006,'Debit','2021-03-12','N','ACTIVE','DEBIT');


UPDATE `Account Table`
SET acct_srt_date = '2017-09-12'
WHERE Acc_ID = 19005;

select * from `account table`;

ALTER TABLE `Account Table`
MODIFY COLUMN Acct_num INT NOT NULL UNIQUE;


-- ----------------------------------------CUSTOMER VERIFICATION QUERIES---------------------------------------------
INSERT INTO customer_verification VALUES(00111,88001,"Done","Pass");
INSERT INTO customer_verification VALUES(00112,88002,"Done","Pass");
INSERT INTO customer_verification VALUES(00118,88003,"In Progress","Fail");
INSERT INTO customer_verification VALUES(00119,88004,"Done","Pass");
INSERT INTO customer_verification VALUES(00120,88005,"In Progress",NULL);
INSERT INTO customer_verification VALUES(00121,88006,"Done","Pass");
INSERT INTO customer_verification VALUES(00122,88007,"Done","Pass");
INSERT INTO customer_verification VALUES(00123,88008,"Done","Pass");


SET FOREIGN_KEY_CHECKS = 1;  -- This function allows you to insert data into either parent/child table by setting the number to 0, then afterwards back to one.
 
 -- --------------------------------------------------------------TRANSACTION QUERIES-----------------------------------------------
 ALTER TABLE transaction_
ADD COLUMN num_of_transaction INT;

-- Generate a SQL query for eligible customers for the Credit card Services. 
-- Credit Card Services are provided only for the customers who has made $100000 in transactions within the last year from the current date
SELECT tran_id, Acc_ID, tran_type, tran_amt, trans_srt_date, last_transaction, total_transactions_amt, 'Approved' AS Verdict 
FROM transaction_ 
WHERE (Timestampdiff(year,trans_srt_date, NOW())) >= 1 AND total_transactions_amt > 100000;


SELECT * FROM transaction_ 
WHERE (Timestampdiff(month,last_transaction, NOW())) >= 06;

INSERT INTO transaction_ VALUES (44000,19001, 'ATM Debit Card WD ',2500, '2020-01-02','2023-04-04', 2500);
INSERT INTO transaction_ VALUES (44007,19001, 'Cash Deposit',150000, '2020-01-02','2023-03-01', 147500);
INSERT INTO transaction_ VALUES (44008,19002, 'Cheque Deposit',124945, '2020-08-03','2021-08-24', 124945);
INSERT INTO transaction_ VALUES (44001,19002, 'Cheque Deposit',5050, '2020-08-03','2021-08-24', 130000);
INSERT INTO transaction_ VALUES (44002,19003, 'Cash Deposit',5700, '2021-11-12','2022-11-01', 89000);
INSERT INTO transaction_ VALUES (44009,19003, 'Cash Deposit',83300, '2021-11-12','2022-11-01', 83300);
INSERT INTO transaction_ VALUES (44003,19004, 'Cash Deposit ',45000, '2021-09-03','2022-09-30', 100000);
INSERT INTO transaction_ VALUES (44010,19004, 'Cash Deposit ',55000, '2021-09-03','2022-09-30', 55000);
INSERT INTO transaction_ VALUES (44004,19005, 'Cash Deposit ',7500, '2020-12-15','2021-12-24', 85000);
INSERT INTO transaction_ VALUES (44011,19005, 'Cheque Deposit',77500, '2020-12-15','2021-12-24',77500);
INSERT INTO transaction_ VALUES (44005,19000, 'Cheque Deposit',5600, '2020-08-22','2021-08-07', 122000);
INSERT INTO transaction_ VALUES (44006,19000, 'Cash Deposit',77000, '2020-08-23','2021-08-07', 199000);

UPDATE transaction_
set total_transactions_amt = 150000
WHERE tran_id = 44007;

select * from transaction_;
-- -----------------------------------------------------------LOAN QUERIES----------------------------------------------------------
INSERT INTO Loan VALUES (55000,19000,500000,'2021-07-10', '2022-07-10',NULL,NULL, 7.5);

INSERT INTO Loan VALUES (55000,19000,500000,'2021-07-10', '2022-07-10',NULL,NULL, 7.5);
INSERT INTO Loan VALUES (55000,19000,500000,'2021-07-10', '2022-07-10',NULL,NULL, 7.5);
INSERT INTO Loan VALUES (55000,19000,500000,'2021-07-10', '2022-07-10',NULL,NULL, 7.5);
INSERT INTO Loan VALUES (55000,19000,500000,'2021-07-10', '2022-07-10',NULL,NULL, 7.5);

UPDATE Loan
SET mthly_payment = (loan_amt / 12 ) + (loan_amt * ((intr_rate / 100) / 12)) -- mthly_payment = loan_amt * (intr_rate / (Timestampdiff(year,loan_srt_date, NOW())))
WHERE loan_id = 55000;

UPDATE loan
SET loan_bal_remain = loan_amt - (mthly_payment * mths_paid);

-- Generate a SQL query where customer and loan and outstanding amount
SELECT A.Acc_ID, C.F_name, C.L_name, L.Loan_id, L.loan_bal_remain FROM `Account Table` AS A
INNER JOIN Loan L 
Using (Acc_ID)
INNER JOIN customer C
USING (cust_id);


-- Generate a SQL query with all details like Customer, account, type, Balance amount based on the transaction.

SELECT C.F_name, C.L_name,C.cust_status, A.Acc_ID, A.Acct_type, L.loan_amt, L.loan_bal_remain, tran_id,tran_type, total_transactions_amt FROM `Account Table` AS A
INNER JOIN Loan L
Using (Acc_ID)
INNER JOIN customer C
USING (cust_id)
INNER JOIN transaction_ T
USING (Acc_ID)
WHERE total_transactions_amt > 1;

select * from loan;

-- -----------------------------------------------------------------------------------------CARD QUERIES-------------------------------------------------
INSERT INTO card VALUES (777000, 19000, 1228000, "2029-09-09", "Visa");
INSERT INTO card VALUES (777001, 19001, 1227540, "2030-08-08", "Midas");
INSERT INTO card VALUES (777002, 19002, 1228960, "2030-07-07", "Midas");
INSERT INTO card VALUES (777003, 19003, 1228876, "2029-06-06", "Midas");
INSERT INTO card VALUES (777004, 19004, 1228239, "2031-01-01", "Visa");
INSERT INTO card VALUES (777005, 19005, 1228645, "2028-07-23", "Visa");

UPDATE card
SET card_type ="Visa Debit"
where card_id = 777000;

SELECT * FROM  card