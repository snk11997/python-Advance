
create database snk ;
create table student ( id int , name varchar(100) , age int )  ;
use snk ;
show tables ;

alter table student
add grade varchar(100) ;

select * from student ;

alter table student 
rename column grade to finalgrade ;  

select * from student where finalgrade= "A" ;

select * from student  where age between 23 and  56 ;


select * from student  where finalgrade> "A" ;


select * from student  where finalgrade> "A" ;

SELECT COUNT(name) total from student ;

SELECT avg(age) total from student ;

SELECT avg(age) total from student  where finalgrade="A" or finalgrade="B" ;

SELECT count(*) From students 
 group by finalgrade ;
 
 SELECT count(name) From students 
 group by finalgrade ;
 
 















