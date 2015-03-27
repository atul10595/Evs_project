import csv
import MySQLdb

MAXCOL = 4   #IMPORTANT

# Open database connection
db = MySQLdb.connect("localhost","root","mohit1995","CSV_SQL")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EVS_DATABASE")

# Create table as per requirement
sql = """CREATE TABLE EVS_DATABASE (BUS_STOP CHAR(20) NOT NULL, BUS_1 CHAR(20), BUS_2 CHAR(20),BUS_3 CHAR(20))"""

cursor.execute(sql)
with open('text.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		l = len(row)
		for p in range(l,MAXCOL) :
			row.append('NULL')
		sql = "INSERT INTO EVS_DATABASE(BUS_STOP,BUS_1, BUS_2, BUS_3) VALUES ('%s', '%s', '%s', '%s')" % (row[0],row[1],row[2],row[3])
		try:
		   # Execute the SQL command
		   cursor.execute(sql)
		   # Commit your changes in the database
		   db.commit()
		except:
		   # Rollback in case there is any error
		   db.rollback()
db.close()