#!/usr/bin/python


# Script pour telecharger City

import MySQLdb

file_ = open('rental.csv', 'w')
file_.write ('rental_id,renatal_date,inventory_id,customer_id,return_date,staff_id\n')
db = MySQLdb.connect( user='etudiants',
                      passwd='etudiants_1',
                      host='192.168.99.100',
                      db='sakila')

cur = db.cursor()

cur.execute("SELECT * FROM rental where rental_date between '2005-08-23 20:00:00' and '2005-08-23 21:00:00' and return_date between '2005-08-23 23:59:00' and '2005-08-24 00:00:00'")

for row in cur.fetchall():
    file_.write(str(row[0])+','+ row[1]+','+ str(row[2])+'\n')

db.close()
file_.close()
