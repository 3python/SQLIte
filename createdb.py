import sqlite3

#Connecting/creating a database called resultsdb.
conn = sqlite3.connect('resultsdb.sqlite')
#Getting a cursor to interact with the database.
c = conn.cursor()
#Creating a table within the database.
c.execute("CREATE TABLE IF NOT EXISTS Results (address text, burglaries integer)")
#Inserting results into the table.
c.execute("INSERT INTO Results VALUES ('Queen Vic',2)")
c.execute("INSERT INTO Results VALUES ('Henry',1)")
c.execute("INSERT INTO Results VALUES ('McQueens',0)")
c.execute("INSERT INTO Results VALUES ('OldHarry',4)")
#Committing the changes to the database.
conn.commit()
#Closing the database.
conn.close()
#Closing the cursor.
c.close()
