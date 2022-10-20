import MySQLdb
con=MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="oPOx028ar",
    db="app")

cur=con.cursor()

cur.execute("""
            CREATE TABLE app.user
            (userid MEDIUMINT NOT NULL AUTO_INCREMENT,
            name VARCHAR(30),
            post VARCHAR(10),
            passworod VARCHAR(20),
            PRIMARY KEY(userid))
            """)


con.commit()

con.close()
