#!/usr/bin/python3
import sys
import MySQLdb
''' Get all rows of a table '''

if __name__ = '__main__':
    r = sys.argv[1]
    p = sys.argv[2]
    db = MySQLdb.connect(host='localhost', user=r, passwd=p, db=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states')
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
