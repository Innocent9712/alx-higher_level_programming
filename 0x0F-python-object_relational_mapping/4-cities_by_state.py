#!/usr/bin/python3
"""
This module runs a script to fetch all cities table
in the database provided along with the state name from the state_id
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities c \
                INNER JOIN states s ON s.id = c.state_id ")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
