#Import sqlite.
import sqlite3

#Connecting to the database.
conn = sqlite3.connect('resultsdb.sqlite')

#Getting a cursor to interact with the database.
c = conn.cursor()

#Printing the results of each row in the database.
#Looping through each database row.
for row in c.execute('SELECT * FROM Results ORDER BY burglaries'):
    #Printing the amount of burglaries that have happened at each house.
    print(u'{1} burglaries have happened at {0}'.format(row[0], row[1]))
    #Printing all the entries for each row.
    print(row)

#Description of the columns in the table.
print(c.description)
#Closing the database.
conn.close()
#Closing the cursor.
#c.close()