create database student;
use student;
create table students(
region_num INT PRIMARY KEY NOT NULL,
name_ VARCHAR(25),
DOB date NOT NULL,
AGE_ INT NOT NULL,
address varchar(25),
mark1 int NOT NULL,
mark2 int NOT NULL,
mark3 int NOT NULL,
average int NOT NULL,
grade varchar(3) not null
);

ALTER TABLE students
MODIFY grade VARCHAR(3);

ALTER TABLE students
MODIFY DOB date;

INSERT INTO students VALUES (1100,"Bob","2000-04-13",13,"Windermere Drive",90,89,91,90,'A+');
INSERT INTO students VALUES (1200,"Mary","2000-01-11",19,"Chester Drive",65,78,85,76,'C-');
INSERT INTO students VALUES (1300,"Ruth","2000-02-23",18,"Mountain Drive",77,59,64,66,'C-');
INSERT INTO students VALUES (1400,"Sam","2000-11-30",20,"Cycle Drive",93,92,91,92,'A');
INSERT INTO students VALUES (1500,"Jill","2000-07-14",17,"Uplift Drive",82,79,85,82,'A');
-- I. Name and Age 
-- II. Name and Marks who scored more than 90
-- iii. Name whose grade= A+ and age=19

     
select AGE_,name_ 
from students;

select name_,mark1,mark2,mark3
from students
where mark1 and mark2 and mark3 > 90;

select name_,grade,AGE_
from students
where AGE_ >= 19 and grade = "A+";
#-----------------------------------------------------------------------------------------------------------

create table customer(
Customer_ID INT PRIMARY KEY NOT NULL,
Customer VARCHAR(25),
Contact Varchar(25),
Address Varchar(25),
City varchar(25) NOT NULL,
Postal varchar(10) NOT NULL,
Country varchar(25) NOT NULL
);

alter table customer
modify Postal varchar(10);

alter table customer
drop column Code_;

update customer
set Postal = "PC-019"
where Customer_ID = 20;

INSERT INTO customer VALUES (1,"Bob","876-555-5555","","Portmore",000,"Germany");
INSERT INTO customer VALUES (2,"Mary","876-444-4444","Chester Drive","Portmore",001,"Germany");
INSERT INTO customer VALUES (3,"Ruth","876-777-7777","Mountain Drive","Portmore",002,"Germany");
INSERT INTO customer VALUES (4,"Sam","876-888-8888","Cycle Drive","Portmore",003,"Germany");
INSERT INTO customer VALUES (5,"Jill","876-555-7777","Uplift Drive","Portmore",004,"Germany");

INSERT INTO customer VALUES (6,"Jack","876-888-5555","Paula Drive","Kingston",005,"France");
INSERT INTO customer VALUES (7,"Dave","876-333-4444","","Kingston",006,"France");
INSERT INTO customer VALUES (8,"Sidd","876-000-7777","Des Drive","Kingston",007,"France");
INSERT INTO customer VALUES (9,"Samuel","876-111-8888","Lupa Drive","Kingston",008,"France");
INSERT INTO customer VALUES (10,"Dilly","876-222-7777","Nah Drive","Kingston",009,"France");

INSERT INTO customer VALUES (11,"Latty","876-888-1111","Uptop Drive","Mandeville",010,"England");
INSERT INTO customer VALUES (12,"Jessica","876-333-8888","Down Drive","Mandeville",011,"England");
INSERT INTO customer VALUES (13,"Daniel","876-000-0000","Back Drive","Mandeville",012,"England");
INSERT INTO customer VALUES (14,"Kiesha","876-111-5555","Side Drive","Mandeville",013,"England");
INSERT INTO customer VALUES (15,"Sabrina","876-222-3333","North Drive","Mandeville",014,"England");

INSERT INTO customer VALUES (16,"Micky","876-999-1111","West Drive","Ocho Rios",015,"Jamaica");
INSERT INTO customer VALUES (17,"Luke","876-454-8888","South Drive","Ocho Rios",016,"Jamaica");
INSERT INTO customer VALUES (18,"David","876-789-0000","East Drive","Ocho Rios",017,"Jamaica");
INSERT INTO customer VALUES (19,"Joseph","876-147-5555","Night Drive","Ocho Rios",018,"Jamaica");
INSERT INTO customer VALUES (20,"Esther","876-852-3333","Morning Drive","Ocho Rios",019,"Jamaica");



select * from customer;

select distinct country from customer;

select customer from customer;
select count(distinct country) as Differnt_Coutries from customer;
select count(country) as Differnt_Coutries from customer;

select Customer_ID, Customer, Contact, Address from customer
WHERE Customer_ID > 5;

select customer_ID, Customer, Contact, Address, country from customer
where country = "Jamaica";
#----------------------------------------------------------------------------------

create table products(
Product_ID INT PRIMARY KEY NOT NULL,
Product_name VARCHAR(25),
Supplier_ID bigint,
Category_ID bigint,
Unit_ INT NOT NULL,
Price decimal NOT NULL
);



ALTER TABLE products
ADD COLUMN Price decimal;

ALTER TABLE products
MODIFY Supplier_ID bigint;

ALTER TABLE products
MODIFY Category_ID bigint;

INSERT INTO products VALUES (1,"Sardine",12000,41000,15,120.00);
INSERT INTO products VALUES (2,"Mackerel",12001,41001,54,90.00);
INSERT INTO products VALUES (3,"Milk",12002,41002,12,165.00);
INSERT INTO products VALUES (4,"Crackers",12003,41003,45,154.00);
INSERT INTO products VALUES (5,"Water",12004,41004,8,100.00);

INSERT INTO products VALUES (6,"Bag Juice",12005,41005,45,120.00);
INSERT INTO products VALUES (7,"Bake Beans",12006,41006,36,110.00);
INSERT INTO products VALUES (8,"Flour",12007,41007,12,79.00);
INSERT INTO products VALUES (9,"Rice",12008,41008,78,174.00);
INSERT INTO products VALUES (10,"Cornmeal",12009,41009,8,100.00);

INSERT INTO products VALUES (11,"Cereal",12010,41010,99,150.00);
INSERT INTO products VALUES (12,"Wine",12011,41011,71,1275.00);
INSERT INTO products VALUES (13,"Bleach",12012,410012,13,132.00);
INSERT INTO products VALUES (14,"Soap",12013,41013,11,89.00);
INSERT INTO products VALUES (15,"Soda",12014,41014,18,100.00);

INSERT INTO products VALUES (16,"Pens",12015,41014,110,80.00);
INSERT INTO products VALUES (17,"Books",12016,41016,71,255.00);
INSERT INTO products VALUES (18,"Sharpener",12017,410017,13,85.00);
INSERT INTO products VALUES (19,"Rubber",12018,41018,11,70.00);
INSERT INTO products VALUES (20,"Stapler",12019,41019,18,190.00);

select * from products;

select product_id, product_name, unit_,  price from products
order by price;

select product_id, product_name, unit_, price FROM products
order by price desc;

select product_id, product_name, unit_, price from products
order by product_name ASC;

select product_id, product_name, unit_, price from products
order by product_name desc;

select min(price) as Minimum_Price from products;

select max(price) as Maximum_Price from products;

select count(*) products from products;

select count(*) products from products
where price > 100;

update products
set Product_name = NULL 
where Product_ID = 1;

select count(*) products from products
where Product_name is not null;

select count(distinct Price) from products;
#----------------------------------------------------------------------------------------------------------
create table orderdetails(
orderdetails_ID INT PRIMARY KEY NOT NULL,
Order_ID VARCHAR(25),
Product_ID INT,
FOREIGN KEY (Product_ID) REFERENCES products(Product_ID) ON DELETE SET NULL,
Quantity INT
);

INSERT INTO orderdetails VALUES (55001,"OD-001",1,41);
INSERT INTO orderdetails VALUES (55002,"OD-002",2,11);
INSERT INTO orderdetails VALUES (55003,"OD-003",6,21);
INSERT INTO orderdetails VALUES (55004,"OD-004",10,10);
INSERT INTO orderdetails VALUES (55005,"OD-005",15,33);
INSERT INTO orderdetails VALUES (55006,"OD-006",11,44);
INSERT INTO orderdetails VALUES (55007,"OD-007",11,25);
INSERT INTO orderdetails VALUES (55008,"OD-006",7,6);
SET FOREIGN_KEY_CHECKS = 1; 

select * from orderdetails;

select sum(Quantity) as Total_Quantity from orderdetails;

select count(Order_ID) as Total from orderdetails
where Product_ID = 11;


select O.orderdetails_ID, O.Order_ID, O.Quantity, P.Product_ID, P.Product_name, P.Unit_, P.Price
from orderdetails O
inner join products P
on O.Product_ID = P.Product_ID;

select avg(P.Price) as Average_Price from orderdetails O inner join products P on O.Product_ID = P.Product_ID;

select Price, Unit_, Product_ID, Product_name
from products
where Price > (select avg(P.Price) as Average_Price from orderdetails O inner join products P on O.Product_ID = P.Product_ID);

#-------------------------------------------------------CASE STUDY-----------------------------------------------------------
create table courses(
CID INT PRIMARY KEY NOT NULL,
course_name VARCHAR(25) Not Null,
category enum ("Basic", "Medium", "Advanced"),
fee decimal Not Null
);

select * from courses;

INSERT INTO courses VALUES (1,"Education","Basic",10000.00);
INSERT INTO courses VALUES (2,"Education","Medium",15000.00);
INSERT INTO courses VALUES (3,"Java","Basic",20000.00);
INSERT INTO courses VALUES (4,"Java","Advanced",14000.00);
INSERT INTO courses VALUES (5,"Law","Medium",33000.00);
INSERT INTO courses VALUES (6,"Law","Advanced",44000.00);
INSERT INTO courses VALUES (7,"Medical Sciences","Medium",25000.00);
INSERT INTO courses VALUES (8,"Medical Sciences","Advanced",60000.00);
INSERT INTO courses VALUES (9,"Sport","Medium",29000.00);
INSERT INTO courses VALUES (10,"Sport","Advanced",45000.00);

UPDATE courses
SET fee = "30000.00" 
WHERE CID = 4;
#-------------------------------------------------------------------------------------------

create table studentmaster(
SID INT PRIMARY KEY NOT NULL,
CID INT,
student_name VARCHAR(10) Not Null,
origin enum ('Local', 'Foreign') NOT NULL,
type_ char(1) NOT NULL
);
select * from studentmaster;

ALTER TABLE studentmaster 
ADD CONSTRAINT FOREIGN KEY (CID)
REFERENCES courses (CID)
ON DELETE SET NULL
ON UPDATE SET NULL;

ALTER TABLE studentmaster
ADD CID INT;

INSERT INTO studentmaster VALUES (55001,'Jamar Chase','Local',"G");
INSERT INTO studentmaster VALUES (55002,"Matt Lefeur",'Foreign',"G");
INSERT INTO studentmaster VALUES (55003,"Jalen Hurts","Foreign","G");
INSERT INTO studentmaster VALUES (55004,'Jason Malmoa',"Local","G");
INSERT INTO studentmaster VALUES (55005,"Tyrone Hill","Foreign","G");
INSERT INTO studentmaster VALUES (55006,"Devontae Smith","Foreign","U");
INSERT INTO studentmaster VALUES (55007,"David Blair","Local","U");
INSERT INTO studentmaster VALUES (55008,"Joseph Brown","Local","U");
INSERT INTO studentmaster VALUES (55009,"Luke Smith","Local","U");
INSERT INTO studentmaster VALUES (55010,"Matthew Barker","Foreign","G");


select * from studentmaster;

update studentmaster
set CID = 1
WHERE SID = 55010;

#-----------------------------------------------------------------------------------------

create table enroll_master(
CID int NOT NULL,
SID int NOT NULL,
FOREIGN KEY (CID) REFERENCES courses(CID),
FOREIGN KEY (SID) REFERENCES studentmaster(SID),
DOE date NOT NULL,
FWF char(1) NOT NULL,
grade enum ("O", "A", "B", "C")
);

INSERT INTO enroll_master VALUES (1,55001,"2023-04-13","Y","O");
INSERT INTO enroll_master VALUES (2,55002,"023-03-18","N","A");
INSERT INTO enroll_master VALUES (3,55003,"2023-08-25","Y","B");
INSERT INTO enroll_master VALUES (4,55004,"2023-05-17","N","C");
INSERT INTO enroll_master VALUES (5,55005,"2023-06-25","Y","O");
INSERT INTO enroll_master VALUES (6,55006,"2023-07-05","N","B");
INSERT INTO enroll_master VALUES (7,55007,"2023-09-20","Y","A");
INSERT INTO enroll_master VALUES (8,55008,"2023-02-12","N","C");
INSERT INTO enroll_master VALUES (9,55009,"2023-01-25","Y","O");
INSERT INTO enroll_master VALUES (1,55010,"2023-11-16","N","A");
INSERT INTO enroll_master VALUES (2,55011,"2023-01-13","Y","A");
INSERT INTO enroll_master VALUES (3,55012,"023-02-18","N","O");
INSERT INTO enroll_master VALUES (4,55013,"2023-03-25","Y","C");
INSERT INTO enroll_master VALUES (5,55014,"2023-04-17","N","C");
INSERT INTO enroll_master VALUES (6,55015,"2023-05-25","Y","A");
INSERT INTO enroll_master VALUES (7,55016,"2023-06-05","N","C");
INSERT INTO enroll_master VALUES (8,55017,"2023-06-20","Y","C");
INSERT INTO enroll_master VALUES (9,55018,"2023-05-12","N","A");
INSERT INTO enroll_master VALUES (5,55019,"2023-04-25","Y","C");
INSERT INTO enroll_master VALUES (3,55020,"2023-03-16","N","A");
INSERT INTO enroll_master VALUES (2,55021,"2023-02-05","N","C");
INSERT INTO enroll_master VALUES (3,55022,"2023-01-20","Y","C");
INSERT INTO enroll_master VALUES (7,55023,"2023-01-12","N","A");
INSERT INTO enroll_master VALUES (7,55024,"2023-09-25","Y","A");
INSERT INTO enroll_master VALUES (7,55025,"2023-09-16","N","A");
INSERT INTO enroll_master VALUES (3,55026,"2023-11-23","Y","C");


select * from enroll_master;

#2,3,10,4 - already done

UPDATE enroll_master
set CID = 1
where SID = 55001;

select * from studentmaster;

#--------------------------------------------------------QUERIES-----------------------------------------------
#1.List the course-wise total no. of Students enrolled. Provide the information only for students of foreign origin and only if the total exceeds 10.

select distinct course_name as Total_Courses from courses; 

select student_name from studentmaster;

select count(student_name) as Total_Num_Students from studentmaster;


select S.SID, C.CID, S.student_name, S.origin, S.type_, C.course_name, C.category
from studentmaster S
inner join courses C
on S.CID = C.CID;

select S.SID, C.CID, S.student_name, S.origin, S.type_, C.course_name, C.category
from studentmaster S
inner join courses C
on C.CID = S.CID
WHERE origin = "Foreign";

#2. List the names of the Students who have not enrolled in the Java course.
select S.SID, C.CID, S.student_name, S.origin, S.type_, C.course_name, C.category
from studentmaster S
inner join courses C
on C.CID = S.CID
WHERE C.course_name != "Java";

#3. List the name of the advanced course where the enrollment by foreign students is the highest.

select C.course_name, count(C.CID) as Course_ID
from studentmaster S
inner join courses C
on C.CID = S.CID
WHERE C.category = "Advanced" and S.origin = "Foreign" 
GROUP BY C.course_name;

#4. List the names of the students who have enrolled for at least one basic course in the current month.

select S.student_name, C.course_name, C.Category, E.DOE from studentmaster As S
inner join courses C
Using(CID)
inner join enroll_master E
using (SID)
WHERE C.category = "Basic" and (Timestampdiff(month,DOE, NOW())) <= 1;

#5. List the names of the Undergraduate, local students who have got a “C” grade in any basic course.
select S.student_name, C.course_name, S.origin, C.Category, S.type_, E.grade from studentmaster As S
inner join courses C
Using(CID)
inner join enroll_master E
using (SID)
WHERE C.category = "Basic" and S.type_ = "U" and S.origin = "Local" and E.grade = "C";

#6. List the names of the courses for which no student has enrolled in the month of May 2023.
SELECT distinct C.course_name
FROM courses C
LEFT JOIN enroll_master E ON C.CID = E.CID
WHERE MONTH(E.DOE) <> 5;

#7. List name, Number of Enrollments, and Popularity for all Courses. Popularity has to be
#displayed as “High” if the number of enrollments is higher than 7, “Medium” if less than
#or equal to 6 and greater than 3, and “Low” if the no.  Is less than 3.
SELECT
    C.course_name,
    COUNT(S.CID) AS enrollment_count,
    CASE
        WHEN COUNT(S.CID) > 4 THEN 'High'
        WHEN COUNT(S.CID) <= 4 AND COUNT(S.CID) > 3 THEN 'Medium'
        WHEN COUNT(S.CID) <= 3 THEN 'Low'
        ELSE 'No Popularity'
    END AS popularity
FROM
    courses C
LEFT JOIN studentmaster S ON C.CID = S.CID
GROUP BY
    C.course_name
ORDER BY
    popularity;
    


#8. List the most recent enrollment details with information on Student Name, Course name, and age of enrollment in days.
select S.student_name, C.course_name, day(E.DOE) as Enrollment from studentmaster as S
inner join courses C
using (CID)
inner join enroll_master E
using (SID)
order by day(E.DOE) DESC;

#9. List the names of the Local students who have enrolled for exactly 3 basic courses.
select S.student_name, C.course_name, S.origin from studentmaster As S
inner join courses C on S.CID = C.CID
WHERE C.category = "Basic" and S.origin = "Local" ;

#10. List the names of the Courses enrolled by all (every) students.
select C.course_name, S.student_name from studentmaster as S
Left Join courses C on S.CID = C.CID;


#11. For those enrollments for which fees have been waived, provide the names of students who have got ‘O’’ grades.
select S.student_name, C.course_name, S.type_, E.grade, E.FWF from studentmaster As S
inner join courses C
Using(CID)
inner join enxroll_master E
using (SID)
WHERE E.FWF = "Y" and E.grade = "O";

#12. List the names of the foreign, undergraduate students who have got a grade of ‘C’ in any basic course.
select S.student_name, C.course_name, S.type_, E.grade, E.FWF, C.category, S. Origin from studentmaster As S
inner join courses C
Using(CID)
inner join enroll_master E
using (SID)
WHERE C.category = "Basic" and E.grade = "C" and S.origin = "Foreign" and S.type_ = "U";

#13. List the course name and total no. of enrollments in the current month.
SELECT c.course_name, count(E.CID) as No_of_Enrollments
FROM courses C
Left Join enroll_master E on C.CID = E.CID
WHERE MONTH (E.DOE) = 11
Group BY C.course_name;

