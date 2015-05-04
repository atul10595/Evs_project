import csv
import MySQLdb

MAXCOL = 2   #IMPORTANT

# Open database connection
db = MySQLdb.connect("localhost","root","shivomthukral","CSV_SQL")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS BUS_STAND_DATA")

# Create table as per requirement
sql = """CREATE TABLE BUS_STAND_DATA (BUS_STAND CHAR(20) NOT NULL, BUS_NO CHAR(20))"""

cursor.execute(sql)
with open('BusStandData.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		l = len(row)
		for p in range(l,MAXCOL) :
			row.append('NULL')
		sql = "INSERT INTO BUS_STAND_DATA (BUS_STAND,BUS_NO) VALUES ('%s', '%s')" % (row[0],row[1])
		try:
		   # Execute the SQL command
		   cursor.execute(sql)
		   # Commit your changes in the database
		   db.commit()
		except:
		   # Rollback in case there is any error
		   db.rollback()

db.close()