show databases;

create database logic;
use logic;

create table student(  
   id INT PRIMARY KEY,
   Name VARCHAR(30),
   gpa DECIMAL(3,2)
   );
   
create table vrmall3(id int ,name varchar(100) , role varchar(100),salary int) ;

select * from vrmall3 ;
insert into vrmall3  values(1,"mani","admin",100000),(2,"mani","admin",100000),(3,"mani","admin",100000),(4,"mani","admin",100000),(5,"ram","manager",10000),
(6,"harini","sales",100000),(7,"pooja","sales",100000),(8,"ramya","hr",3000000),
(9,"mani","admin",100000),(10,"ragu","ceo",8000000),(11,"ashok","hr",2200000);
   
delete from vrmall3 where role="admin" ;
delete from vrmall3 where role="ceo" ;

select * from vrmall3 ;



