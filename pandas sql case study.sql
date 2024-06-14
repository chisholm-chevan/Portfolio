# 4 tables - Sales, Customers, Products and Stores - Auto Parts Store
Create database Case_Study;
Use Case_Study;
Create Table Customers(
Customer_ID int primary key not null,
FName varchar(25),
Lname varchar(25)
);

insert into Customers values
(0001,"Dave","Bernard"),
(0002,"Michale","Lindo"),
(0003,"Sasha","Brown"),
(0004,"Luke","Littler"),
(0005,"Chris","Brown"),
(0006,"Diogo","Dalot"),
(0007,"Ashely","Cole"),
(0008,"John","Terry"),
(0009,"Vic","Vangio"),
(0010,"Tom","Brady");



Create Table Sales(
Sales_ID int primary key not null,
Customer_ID Int not null,
Sale_cost int,
sale_date date,
Product_ID int,
Store_ID int,
FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID) ON DELETE CASCADE on update cascade,
FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID) ON DELETE CASCADE on update cascade
# Add store ID
);


Alter table sales
Add column Amount_Sold int;

ALTER TABLE Sales 
ADD CONSTRAINT FOREIGN KEY (Store_ID)
REFERENCES Stores (Store_ID)
ON DELETE cascade 
on update cascade;


insert into sales values
(11001,0001,35000,"2023-02-02",22001,331),
(11002,0001,35000,"2024-01-11",22001,331),
(11003,0002,37000,"2023-12-27",22010,201),
(11004,0003,9500,"2024-01-13",22008, 453),
(11005,0004,10000,"2024-01-09",22009,678),
(11006,0005,22000,"2023-12-02",22007,909),#
(11007,0005,7000,"2024-01-07",22004, 331),
(11008,0006,15000,"2024-01-01",22003,201),
(11009,0007,10000,"2024-01-19",22002,453),
(11010,0008,10000,"2023-12-30",22002,909),
(11011,0009,50000,"2023-12-15",22006,909),
(11012,0010,30000,"2023-12-16",22005,331);

Update sales
set sale_cost = 100000
where Sales_ID = 11011;

SET FOREIGN_KEY_CHECKS = 1; 

Create Table Products(
Product_ID int primary key not null,
Product varchar(25),
Car_Item_class enum('Honda','Audi','Jeep','Toyota','Subaru'),
produuct_cost int
);

insert into Products values
(22001,"Tires","Audi",35000),
(22002,"Break Fluid","Honda",10000),
(22003,"Engine oil","Jeep",15000),
(22004,"Windshield Wiper Blades","Toyota",7000),
(22005,"Tires","Toyota",30000),
(22006,"Transmission Box","Subaru",50000),
(22007,"Rims","Subaru",22000),
(22008,"Spoiler","Jeep",9500),
(22009,"Engines","Audi",100000),
(22010,"Tires","Honda",37000);



Create Table Stores(
Store_ID int primary key not null,
Store_Name varchar(25),
Store_Location varchar(25),
Store_Manager varchar(25)
);

insert into Stores values
(201,"One Fire Auto Parts","Jamaica", "Chris A."),
(331,"Trinity Auto Parts","Trinidad", "Mike W."),
(453,"Baha Auto Parts","Bahamas", "Tina B."),
(678,"Cyman Auto Parts","Caymanas", "David D."),
(909,"One Rep Auto Parts","Dominican Republic", "Angela A.");


# Inner Join
-- Returns records that have matching values in both tables
select officers.officer_name, officers.address, students.course_name
from officers
inner join students
on officers.officer_id = students.student_id;

# Left Join
-- The LEFT OUTER JOIN returns all rows from the left hand table specified in the ON
-- condition and only those rows from the other table where the join condition is fulfilled.
select officers.officer_name, officers.address, students.course_name
from officers
left join students
on officers.officer_id = students.student_id;

select S.SID, C.CID, S.student_name, S.origin, S.type_, C.course_name, C.category
from studentmaster S
inner join courses C
on S.CID = C.CID;
#-----------------------------------------------------------------------------------------

select S.sale_cost,C.Customer_ID
from Sales S
left join Customers C
on S.Customer_ID = C.Customer_ID;



select * from Stores;
select * from Sales;
select * from Products;
select * from Customers;

# Chart - Showing the total amount per store
select sum(Sales.Sale_Cost) as Total_Figures,Stores.Store_ID
from Stores
Join Sales
on Stores.Store_ID = Sales.Store_ID
group by Stores.Store_ID;


# Chart - SHowing the best selling product
select sum(Sales.Sale_Cost) as Total_Figures,Products.product_cost as Unit_Cost,Products.Product_ID
from Products
Join Sales
on Products.Product_ID = Sales.Product_ID
group by Products.Product_ID;




# Group the data by product category and calculate average sales
select Products.Product_ID,Products.Product,Products.Car_Item_class,Sales.Sales_ID,Sales.Sale_Cost
from Products
Join Sales
on Products.Product_ID = Sales.Product_ID;

# Group the data by customer segment and calculate total sales
select Customers.Customer_ID,Customers.Fname,Customers.Lname,Sales.Sales_ID,Sales.Sale_Cost
from Customers
Join Sales
on Customers.Customer_ID = Sales.Customer_ID;

select sum(Sale_Cost) as Total_Revenue from Sales;

SELECT S.Sales_ID, S.sale_cost,S.sale_date,S.Store_ID,ST.Store_Name,ST.STore_Location,C.Customer_ID,C.Fname,C.Lname, P.Product_ID,P.Product,P.Car_Item_class FROM Sales AS S
INNER JOIN Customers C
Using (Customer_ID)
INNER JOIN Products P
USING (Product_ID)
INNER JOIN Stores ST
USING (Store_ID);

SELECT S.sale_cost, P.Product_ID,P.Product
FROM Sales as S
JOIN Products as P 
ON S.Product_ID = P.Product_ID;

SELECT sum(S.sale_cost) as Total_A, P.Product_ID,P.Product
FROM Sales S
JOIN Products P 
ON S.Product_ID = P.Product_ID
group by P.Product_ID;
        
SELECT sum(S.sale_cost),P.Product
FROM Sales S
JOIN Products P 
ON S.Product_ID = P.Product_ID
group by P.Product_ID;

SELECT sum(sale_cost) FROM Sales;
