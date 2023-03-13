#!/usr/bin/python3
import sys
import MySQLdb

db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
cur.execute('SELECT * FROM states')
states = cur.fetchall()
for state in states:
    print(state)
