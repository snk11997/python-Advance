  
use mani ;

create table emp4( id int primary key  auto_increment, ename varchar(30) NOT null ,    -- you must enter the ename
job_desc varchar(20)  default "unassigned" ,
salary int check (salary>10000) , pan varchar(10) unique  ) ;  


select*from emp4 ;  

insert into emp4(ename,pan,salary) values ("naveen", "rrff" , 1200000 ) ;
insert into emp4(ename,pan,salary) values ("naveen", "r66f" , 12000 ) ;




