import MySQLdb
con=MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="oPOx028ar",
    db="app")

cur=con.cursor()

cur.execute("""
            CREATE TABLE app.schedule
            (scheduleid MEDIUMINT NOT NULL AUTO_INCREMENT,
            userid INTEGER REFERENCES user(userid),
            schedule VARCHAR(30),
            PRIMARY KEY(scheduleid))
            """)


con.commit()

con.close()
