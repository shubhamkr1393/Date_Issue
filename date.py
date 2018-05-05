#########################################################################################################################################
# Databricks notebook source
#Get last day of previous month.
import datetime
today = datetime.date.today()
print today
first = today.replace(day=1)
print first
lastMonth = first - datetime.timedelta(days=1)
print lastMonth
print lastMonth.strftime("%Y%m")

Output:
2018-05-05
2018-05-01
2018-04-30
201804
#########################################################################################################################################
# COMMAND ----------
#Command to convert string to date data type, date to string data type.
import datetime
cdl_effective_date = '2012-01-05'
cdl_date = cdl_effective_date
print "cdl_date of type: "+ str(type(cdl_date))
date_received = datetime.datetime.strptime(cdl_date, "%Y-%m-%d").date()
restricted_date = date_received.replace(day=1) - datetime.timedelta(days=1)
print restricted_date
print "restricted_date of type: "+ str(type(restricted_date))
restricted_date_str = restricted_date.strftime('%Y%m%d') 
print restricted_date_str
print "restricted_date_str of type: "+ str(type(restricted_date_str))

Output:
cdl_date of type: <type 'str'>
2011-12-31
restricted_date of type: <type 'datetime.date'>
20111231
restricted_date_str of type: <type 'str'>
#########################################################################################################################################
# COMMAND ----------
#Find start and end date of the month
cdl_effective_date = '2018-05-20'
date_list = cdl_effective_date.split('-')
if int(date_list[1]) != 12:
  month_range  = monthrange(int(date_list[0]), int(date_list[1])+1)
else:
  month_range  = monthrange((int(date_list[0])+1), 1)
  date_list[0] = str(int(date_list[0])+1)
  date_list[1] = 0

if int(date_list[1]) < 10:
  date_list[1] = "0" + str(int(date_list[1])+1)
startDate = str(date_list[0]+"-"+date_list[1]+"-"+"01")
endDate= str(date_list[0]+"-"+date_list[1]+"-"+str(month_range[1]))
print startDate
print endDate

Output:
2018-06-01
2018-06-30
#########################################################################################################################################
#Major Issue I faced during conversion (%m and %M are different)
#Error Type-1
import datetime
cdl_effective_date = '2018-12-20'
date_received = datetime.datetime.strptime(cdl_effective_date, "%Y-%m-%d").date()
print (date_received)
date_received_str = date_received.strftime('%Y%M%d') 
print (date_received_str)

Output:
2018-12-20
20180020
#strftime('%Y%M%d') set month value as zero zero (00) by default.
#########################################################################################################################################
#error Type-2
import datetime
cdl_effective_date = '2018-12-20'
date_received = datetime.datetime.strptime(cdl_effective_date, "%Y-%M-%d").date()
print (date_received)
date_received_str = date_received.strftime('%Y%M%d') 
print (date_received_str)

Output:
2018-01-20
20180020
#strptime(cdl_effective_date, "%Y-%M-%d").date() set month value as '01' by default.
#########################################################################################################################################
#Error Type-3
import datetime
cdl_effective_date = '2018-12-20'
date_received = datetime.datetime.strptime(cdl_effective_date, "%Y-%M-%d").date()
print (date_received)
date_received_str = date_received.strftime('%Y%m%d') 
print (date_received_str)

Output:
2018-01-20
20180120
#########################################################################################################################################
#Correct code
import datetime
cdl_effective_date = '2018-12-20'
date_received = datetime.datetime.strptime(cdl_effective_date, "%Y-%m-%d").date()
print (date_received)
date_received_str = date_received.strftime('%Y%m%d') 
print (date_received_str)

Output:
2018-12-20
20181220
#########################################################################################################################################
from datetime import datetime
oldFormat = "26JAN2018"
datetime_object = datetime.strptime(oldFormat, '%d%b%Y')
print datetime_object

Output:
2018-01-26 00:00:00
#########################################################################################################################################
