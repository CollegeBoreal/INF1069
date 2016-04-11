#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect( user='etudiants', 
                      passwd='etudiants_1',
                      host='192.168.99.100',
                      db='sakila')

cur = db.cursor()

cur.execute("SELECT * FROM country")

for row in cur.fetchall():
    print row[0]

db.close()
