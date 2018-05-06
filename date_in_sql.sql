#########################################################################################################################################
%sql
create table if not exists demo(id string, dates string);
insert into demo values('101','2017-12-05');
insert into demo values('102','2017-10-05');
insert into demo values('102','2017-11-25');
select * from demo;
Output:
id	dates
102	2017-11-25
102	2017-10-05
101	2017-12-05
#########################################################################################################################################
%sql
select dates, day(TO_DATE(CAST(UNIX_TIMESTAMP(dates, 'yyyy-mm-dd') AS TIMESTAMP))) from demo;
Output:
dates	dayofmonth(to_date(CAST(unix_timestamp(demo.`dates`, 'yyyy-mm-dd') AS TIMESTAMP)))
2017-11-25	25
2017-10-05	5
2017-12-05	5
#########################################################################################################################################
%sql
select dates, day(TO_DATE(CAST(UNIX_TIMESTAMP(dates, 'yyyy-mm-dd') AS TIMESTAMP))) from demo;
Output:
dates	      month(to_date(CAST(unix_timestamp(demo.`dates`, 'yyyy-mm-dd') AS TIMESTAMP)))
2017-11-25	1
2017-10-05	1
2017-12-05	1
---to_date(CAST(unix_timestamp(demo.`dates`, 'yyyy-mm-dd') AS TIMESTAMP)) will always give month number as 1.
#########################################################################################################################################
%sql
select dates, month(TO_DATE(CAST(UNIX_TIMESTAMP(dates, 'yyyy-MM-dd') AS TIMESTAMP))) from demo;
Output:
dates	      month(to_date(CAST(unix_timestamp(demo.`dates`, 'yyyy-MM-dd') AS TIMESTAMP)))
2017-11-25	11
2017-10-05	10
2017-12-05	12
---to_date(CAST(unix_timestamp(demo.`dates`, 'YYYY-MM-dd') AS TIMESTAMP)) will give actual month number.
#########################################################################################################################################
%sql
select dates, year(TO_DATE(CAST(UNIX_TIMESTAMP(dates, 'yyyy-MM-dd') AS TIMESTAMP))) from demo;
Output:
dates	      year(to_date(CAST(unix_timestamp(demo.`dates`, 'YYYY-MM-dd') AS TIMESTAMP)))
2017-11-25	2017
2017-10-05	2017
2017-12-05	2017
#########################################################################################################################################
%sql
drop table if exists demo;
create table if not exists demo(id string, month string, year string);
insert into demo values('101','05','2017');
insert into demo values('102','10','2017');
insert into demo values('103','12','2017');
#########################################################################################################################################
#Get date from month and year.
%sql
select to_date(cast(year||"-"|| case when length(month) <2 then "0"||month else month end||"-01" as date),"YYYY-MM-DD") as date,year,month from demo
Output:
date	      year	month
2017-05-01	2017	05
2017-12-01	2017	12
2017-10-01	2017	10
#########################################################################################################################################
