#!/usr/bin/python3
"""
This module runs a script to fetch all states table
in the database provided where name matches a provided value
This script is succeptible to SQL injection attack
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    if len(argv) == 5:
        db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                             db=argv[3], charset='utf8')
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name = '{:s}' ORDER BY id"
                    .format(argv[4]))
        states = cur.fetchall()
        for state in states:
            if state[1] == argv[4]:
                print(state)
        cur.close()
        db.close()
