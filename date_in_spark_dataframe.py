###########################################################################################################################################
%sql
drop table if exists demo;
create table if not exists demo(id string, dates string);
insert into demo values('101','2017-12-05');
insert into demo values('102','2017-10-05');
insert into demo values('103','2017-11-25');
insert into demo values('104','2017-01-05');
insert into demo values('105','2017-01-31');
insert into demo values('106','2017-02-01');
###########################################################################################################################################
#Convert string to date format and then change the formate to 'yyyy-dd-mm'-Correct result
%python
from pyspark.sql.functions import *
df = spark.sql("select * from demo")
df = df.withColumn('dates_formated', date_format(to_timestamp(df.dates, "yyyy-MM-dd"), "yyyy-dd-MM").cast("string"))
display(df)
OR
%python
from pyspark.sql.functions import *
df = spark.sql("select * from demo")
df = df.withColumn('dates_formated', date_format(to_timestamp(df.dates, "yyyy-mm-dd"), "yyyy-dd-mm").cast("string"))
display(df)
Output:
id	dates	      dates_formated
103	2017-11-25	2017-25-11
102	2017-10-05	2017-05-10
101	2017-12-05	2017-05-12
105	2017-01-31	2017-31-01
106	2017-02-01	2017-01-02
104	2017-01-05	2017-05-01
#########################################################################################################################################
#Error-1
%python
from pyspark.sql.functions import *
df = spark.sql("select * from demo")
df = df.withColumn('dates_formated', date_format(to_timestamp(df.dates, "yyyy-MM-dd"), "yyyy-dd-mm").cast("string"))
display(df)
Output:
id	dates	      dates_formated
103	2017-11-25	2017-25-00
102	2017-10-05	2017-05-00
101	2017-12-05	2017-05-00
105	2017-01-31	2017-31-00
106	2017-02-01	2017-01-00
104	2017-01-05	2017-05-00
#to_timestamp(df.dates, "yyyy-MM-dd"), "yyyy-dd-mm")- It will assign value of month as '00'
########################################################################################################################################
Error-2
%python
from pyspark.sql.functions import *
df = spark.sql("select * from demo")
df = df.withColumn('dates_formated', date_format(to_timestamp(df.dates, "yyyy-mm-dd"), "yyyy-dd-MM").cast("string"))
display(df)
Output:
id	dates	      dates_formated
103	2017-11-25	2017-25-01
102	2017-10-05	2017-05-01
101	2017-12-05	2017-05-01
105	2017-01-31	2017-31-01
106	2017-02-01	2017-01-01
104	2017-01-05	2017-05-01
#to_timestamp(df.dates, "yyyy-mm-dd"), "yyyy-dd-MM")- It will assign value of month as '01'
########################################################################################################################################
%python
from pyspark.sql.functions import *
df = spark.sql("select * from demo")
df = df.withColumn('dates_formated', date_format(to_timestamp(df.dates, "yyyy-MM-dd"), "yyyy-DD").cast("string"))
display(df)
Output:
id	dates	      dates_formated
103	2017-11-25	2017-329
102	2017-10-05	2017-278
101	2017-12-05	2017-339
105	2017-01-31	2017-31
106	2017-02-01	2017-32
104	2017-01-05	2017-05
#to_timestamp(df.dates, "yyyy-MM-dd"), "yyyy-DD")- It will give days count wrt year i.e. 25th Nov is 329th day of year.
########################################################################################################################################
%python
from pyspark.sql.functions import *
df = spark.sql("select * from demo")
df = df.withColumn('dates_formated', date_format(to_timestamp(df.dates, "yyyy-mm-dd"), "yyyy-DD").cast("string"))
display(df)
Output:
id	dates	      dates_formated  
103	2017-11-25	2017-25
102	2017-10-05	2017-05
101	2017-12-05	2017-05
105	2017-01-31	2017-31
106	2017-02-01	2017-01
104	2017-01-05	2017-05
#to_timestamp(df.dates, "yyyy-mm-dd"), "yyyy-DD")- It will give days count wrt month i.e. 25th Nov is 25th day of the month.
########################################################################################################################################
%python
from pyspark.sql.functions import *
df = spark.sql("select * from demo")
df = df.withColumn('dates_formated', date_format(to_timestamp(df.dates, "yyyy-MM-dd"), "yyyy-DD-mm").cast("string"))
display(df)
Output:
id	dates	      dates_formated  
103	2017-11-25	2017-329-00
102	2017-10-05	2017-278-00
101	2017-12-05	2017-339-00
105	2017-01-31	2017-31-00
106	2017-02-01	2017-32-00
104	2017-01-05	2017-05-00
########################################################################################################################################
%python
from pyspark.sql.functions import *
df = spark.sql("select * from demo")
df = df.withColumn('dates_formated', date_format(to_timestamp(df.dates, "yyyy-MM-dd"), "yyyy-DD-MM").cast("string"))
display(df)
Output:
id	dates	      dates_formated  
103	2017-11-25	2017-329-11
102	2017-10-05	2017-278-10
101	2017-12-05	2017-339-12
105	2017-01-31	2017-31-01
106	2017-02-01	2017-32-02
104	2017-01-05	2017-05-01
########################################################################################################################################
%python
from pyspark.sql.functions import *
df = spark.sql("select * from demo")
df = df.withColumn('dates_formated', date_format(to_timestamp(df.dates, "yyyy-mm-dd"), "yyyy-DD-mm").cast("string"))
display(df)
Output:
id	dates	      dates_formated  
103	2017-11-25	2017-25-11
102	2017-10-05	2017-05-10
101	2017-12-05	2017-05-12
105	2017-01-31	2017-31-01
106	2017-02-01	2017-01-02
104	2017-01-05	2017-05-01
########################################################################################################################################
%python
from pyspark.sql.functions import *
df = spark.sql("select * from demo")
df = df.withColumn('dates_formated', date_format(to_timestamp(df.dates, "yyyy-mm-dd"), "yyyy-DD-MM").cast("string"))
display(df)
Output:
id	dates	      dates_formated  
103	2017-11-25	2017-25-01
102	2017-10-05	2017-05-01
101	2017-12-05	2017-05-01
105	2017-01-31	2017-31-01
106	2017-02-01	2017-01-01
104	2017-01-05	2017-05-01
#######################################################################################################################################
%python
from pyspark.sql.functions import *
df = spark.sql("select * from demo")
df = df.withColumn('dates_formated', date_format(to_timestamp(df.dates, "yyyy-mm-DD"), "yyyy-dd-mm").cast("string"))
display(df)
Output:
id	dates	      dates_formated  
103	2017-11-25	2017-25-11
102	2017-10-05	2017-05-10
101	2017-12-05	2017-05-12
105	2017-01-31	2017-31-01
106	2017-02-01	2017-01-02
104	2017-01-05	2017-05-01
########################################################################################################################################
%python
from pyspark.sql.functions import *
df = spark.sql("select * from demo")
df = df.withColumn('dates_formated', date_format(to_timestamp(df.dates, "yyyy-mm-DD"), "yyyy-dd-MM").cast("string"))
display(df)
Output:
id	dates	      dates_formated  
103	2017-11-25	2017-25-01
102	2017-10-05	2017-05-01
101	2017-12-05	2017-05-01
105	2017-01-31	2017-31-01
106	2017-02-01	2017-01-01
104	2017-01-05	2017-05-01
########################################################################################################################################
%python
from pyspark.sql.functions import *
df = spark.sql("select * from demo")
df = df.withColumn('dates_formated', date_format(to_timestamp(df.dates, "yyyy-MM-DD"), "yyyy-dd-mm").cast("string"))
display(df)
Output:
id	dates	      dates_formated  
103	2017-11-25	null
102	2017-10-05	null
101	2017-12-05	null
105	2017-01-31	2017-31-00
106	2017-02-01	null
104	2017-01-05	2017-05-00
########################################################################################################################################
%python
from pyspark.sql.functions import *
df = spark.sql("select * from demo")
df = df.withColumn('dates_formated', date_format(to_timestamp(df.dates, "yyyy-MM-DD"), "yyyy-dd-MM").cast("string"))
display(df)
Output:
id	dates	      dates_formated  
103	2017-11-25	null
102	2017-10-05	null
101	2017-12-05	null
105	2017-01-31	2017-31-01
106	2017-02-01	null
104	2017-01-05	2017-05-01
########################################################################################################################################
%sql
drop table if exists demo;
create table if not exists demo(id string, dates string);
insert into demo values('101','2017-JAN-05');
insert into demo values('102','2017-AUG-05');
insert into demo values('103','2017-NOV-25');
insert into demo values('104','2017-DEC-05');
########################################################################################################################################
%python
from pyspark.sql.functions import *
df = spark.sql("select * from demo")
df = df.withColumn('dates_formated', date_format(to_timestamp(df.dates, "yyyy-MMM-dd"), "yyyy-MM-dd").cast("string"))
display(df)
Output:
id	dates	      dates_formated  
102	2017-AUG-05	2017-08-05
101	2017-JAN-05	2017-01-05
103	2017-NOV-25	2017-11-25
104	2017-DEC-05	2017-12-05
########################################################################################################################################
