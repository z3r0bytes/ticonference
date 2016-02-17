#!/usr/bin/python
import telerivet
import sys
import mysql.connector

cnx = mysql.connector.connect(user='root', password='kefjeuh',
                              host='127.0.0.1',
                              database='asterisk')
cursor = cnx.cursor()
query = ("SELECT tip FROM asterisk.tips WHERE sent = 0")
cursor.execute(query)

for row in cursor.fetchall():
    print row[0]
cursor.close()


cursor = cnx.cursor()
query2 = ("SELECT phoneno FROM asterisk.users")
cursor.execute(query2)

phonenos = []

tr = telerivet.API("ISukluPKgiudBVk3j63fe7ti8NJT8MVP")
project = tr.initProjectById("PJ59808a2fd4431a63")

count = 0
for row2 in cursor.fetchall():
    phonenos.append("\"" + row2[0] + "\"")
    project.sendMessages(
     content =  row[0],
     to_numbers = [phonenos[count]],
     is_template = True
    )
    count+=1
    print "sent to " + row2[0]
 
cursor.close()
cnx.close()

