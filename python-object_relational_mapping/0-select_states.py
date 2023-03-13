#!/usr/bin/python3
'''get all rows of a table'''


import sys
import MySQLdb

r = sys.argv[1]
p = sys.argv[2]
db = MySQLdb.connect(host='localhost', user=r, passwd=p, db=sys.argv[3])
cur = db.cursor()
cur.execute('SELECT * FROM states')
states = cur.fetchall()
for state in states:
    print(state)
