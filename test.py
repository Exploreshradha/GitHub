import sqlite3

conn = sqlite3.connect('employee.db')

c=conn.cursor()

c.execute(""" CREATE TABLE EMP(
		FIRST_NAME TEXT,
		LAST_NAME TEXT,
		PAY INTEGER
	)""")
CONN.COMMIT()

CONN.CLOSE()
