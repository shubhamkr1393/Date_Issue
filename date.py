# Databricks notebook source
import datetime
today = datetime.date.today()
print today
first = today.replace(day=1)
print first
lastMonth = first - datetime.timedelta(days=1)
print lastMonth
print lastMonth.strftime("%Y%m")

# COMMAND ----------

import datetime
cdl_effective_date = '2012-01-05'
cdl_date = cdl_effective_date
date_received = datetime.datetime.strptime(cdl_date, "%Y-%m-%d").date()
restricted_date = date_received.replace(day=1) - datetime.timedelta(days=1)
print restricted_date
print type(restricted_date)
restricted_date_str = restricted_date.strftime('%Y%m%d') 
print restricted_date_str
print type(restricted_date_str)
