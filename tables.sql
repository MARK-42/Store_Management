DROP TABLE tabEmployee;
DROP SEQUENCE employeeSeq;
DROP TABLE tabCustomer;
DROP SEQUENCE customerSeq;
DROP TABLE tabBill;
DROP SEQUENCE billSeq;
DROP TABLE tabProductStock;
DROP TABLE tabProductRegister;

create table tabEmployee(
	employeeId number(4) NOT NULL PRIMARY KEY,
	firstName varchar2(15) NOT NULL,
	lastName varchar2(15) NOT NULL,
    username varchar2(15) NOT NULL UNIQUE,
    password varchar2(40) NOT NULL,
	phoneNumber number(11) NOT NULL UNIQUE,
    address varchar2(30) NOT NULL,
    email varchar2(20) NOT NULL UNIQUE,
    salary number(10) NOT NULL,
    isManager char(1) NOT NULL
);
insert into tabEmployee values(1, 'owner', 'malik', 'USER', 'CF55D79929C2B5CDB13271782076FAAB487FADA0', 1234, 'addr', 'qwer', 0, 'Y');
CREATE SEQUENCE employeeSeq
MINVALUE 1
START WITH 1
INCREMENT BY 1
CACHE 10;

create table tabCustomer(
	customerId number(4) NOT NULL PRIMARY KEY,
	firstName varchar2(15) NOT NULL,
	lastName varchar2(15) NOT NULL,
	phoneNumber number(11) NOT NULL UNIQUE,
    address varchar2(30) NOT NULL,
    email varchar2(20) NOT NULL UNIQUE,
    totalAmount number(15)
);

CREATE SEQUENCE customerSeq
MINVALUE 1
START WITH 1
INCREMENT BY 1
CACHE 10;

create table tabBill(
	billId number(10) NOT NULL PRIMARY KEY,
	customerId number(4) NOT NULL,
	employeeId number(4) NOT NULL,
    amount number(10) NOT NULL,
    totalItems number(4) NOT NULL,
	paymentMethod varchar2(10) NOT NULL,
    billTime varchar2(5) NOT NULL,
    billDate varchar2(10) NOT NULL
);

CREATE SEQUENCE billSeq
MINVALUE 1
START WITH 1
INCREMENT BY 1
CACHE 10;

create table tabProductStock(
    productId varchar2(20) NOT NULL PRIMARY KEY,
    productName varchar2(20) NOT NULL,
    catagory varchar2(20) NOT NULL,
    totalQuantity int NOT NULL,
    price float(2) NOT NULL,
    weight float(2) NOT NULL
);

create table tabProductRegister(
    productId varchar2(20) NOT NULL,
    billId number(10) NOT NULL,
    quantity int NOT NULL,
    sellPrice float(2) NOT NULL
);

commit;