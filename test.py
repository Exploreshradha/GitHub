import sqlite3

#conn = sqlite3.connect('employee.db')
conn = sqlite3.connect(':memory:')

c= conn.cursor()
c.execute(""" CREATE TABLE EMP(
		FIRST_NAME TEXT,
		LAST_NAME TEXT,
		PAY INTEGER
	)""")


conn.commit()
conn.close()
