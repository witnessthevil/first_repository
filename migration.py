import mysql.connector
import boto3 
from secret2 import access_key, secret_access_key
import pandas as pd

connection = mysql.connector.connect(host='localhost',username='root',password='uttalogical99',database='new_project2')
cursor1 = connection.cursor(buffered=True)
cursor2 = connection.cursor()
cursor1.execute("""select * from seventh_game""")
cursor2.execute("""SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'seventh_game' order by ordinal_position""")

list1 = [i for i in cursor1]
list2 = [j[0] for j in cursor2]

first_game = pd.DataFrame(list1, columns=list2)
first_game.to_csv('seventh_game.csv',index=False)
testfile = 'seventh_game.csv'
sql_bucket = 'mymymysqlsqlsqlsqlbucket'
client = boto3.client('s3', 
aws_access_key_id = access_key, 
aws_secret_access_key = secret_access_key)
client.upload_file(testfile,sql_bucket,testfile)

