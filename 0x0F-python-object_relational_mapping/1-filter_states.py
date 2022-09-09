#!/usr/bin/python3
"""
This module runs a script to fetch all states table
in the database provided where name starts with 'N'
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) == 4:
        db = MySQLdb.connect(host='localhost', user=argv[1],
                             passwd=argv[2], db=argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE states.name LIKE 'N%'")
        states = cur.fetchall()
        for state in states:
            print(state)
