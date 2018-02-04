#!/usr/bin/python

#mysql -u seniordesign -p -h den1.mysql5.gear.host
#CREATE TABLE EMR (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(25), age INT(9), problem VARCHAR(256));.

import MySQLdb
print("mysqldb is installed")
# Open database connection
db = MySQLdb.connect("den1.mysql5.gear.host","seniordesign","00000!","seniordesign")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Add colums by altering the table
#cursor.execute("ALTER TABLE EMR ADD position VARCHAR(40)")

# Drop a colums by altering the table
#cursor.execute("ALTER TABLE EMR DROP COLUMN position")

# Updating: don't forget to commit the change to the database
cursor.execute("UPDATE EMR SET problem = 'Stupid and Ugly' WHERE id = 1")
db.commit()

# Show all, fetch all and print all
cursor.execute("SELECT * FROM EMR")
results = cursor.fetchall()
for row in results:
      pid = row[0]
      name = row[1]
      age = row[2]
      problem = row[3]
      # Now print fetched result
      print "id=%s,name=%s,age =%s,problem = %s" % (pid, name,age,problem)

# disconnect from server
db.close()