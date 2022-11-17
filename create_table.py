import mysql.connector
import os,glob


db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='hmdadmin@2002',
    database="harsh"
)
if(db.is_connected):
    print("Connected")
else:
    print("No")

mycursor=db.cursor()

mycursor.execute("CREATE TABLE TEST(SYMBOL varchar(20),SERIES varchar(2),OPEN float,HIGH float,LOW float,CLOSE float,LAST float,PREVCLOSE float,TOTTRDQTY int,TOTTRDVAL float,TIMESTAMP date,TOTALTRADES int,ISIN varchar(20))")