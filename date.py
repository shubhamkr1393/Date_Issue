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
