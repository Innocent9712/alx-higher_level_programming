#!/usr/bin/python3
"""
This module runs a script to fetch all states table
in the database provided where name starts with 'N'
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE 'N%'")
    states = cur.fetchall()
    for state in states:
        if state[1][0] == 'N':
            print(state)
    cur.close()
    db.close()
