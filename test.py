import sqlite3
import csv
import pandas

conn = sqlite3.connect('TEST.db')
#conn = sqlite3.connect(':memory:')

c= conn.cursor()
c.execute(""" CREATE TABLE EMP(
		FIRST_NAME TEXT,     LAST_NAME TEXT, 		PAY INTEGER 	)""")
c.execute("Insert into EMP values ('abc', 'last', 123)")
c.execute("Insert into EMP values ('abcd', 'last2', 1234)")
c.execute("Select * from EMP")
#print(c.fetchall())
#d='Select * from EMP'
result= pandas.read_sql_query("Select * from EMP",conn)
result.to_csv("EmpTable.CSV")

conn.commit()
conn.close()
