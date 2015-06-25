'''
Created on 25 de jun de 2015

@author: Fabricio
'''
import datetime
import mysql.connector


cnx = mysql.connector.connect(user='root', password='86198786',
                              host='127.0.0.1',
                              database='qt_db')
cursor = cnx.cursor()

query = ("SELECT nome, idade FROM cadastro ")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

cursor.execute(query)

for (nome, idade) in cursor:
  print( nome, idade)

cursor.close()
cnx.close()