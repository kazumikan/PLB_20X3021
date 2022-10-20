import MySQLdb
con=MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="oPOx028ar",
    db="app")

cur=con.cursor()

cur.execute("""
            CREATE TABLE app.time
            (starttime DATETIME NOT NULL,
            endtime DATETIME,
            scheduleid INTEGER REFERENCES schedule(scheduleid))
            """)


con.commit()

con.close()
