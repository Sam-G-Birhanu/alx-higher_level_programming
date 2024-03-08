#!/usr/bin/python3
"""
Lists all states that start with N from  hbtn_0e_0_usa.
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb
if __name__ == '__main__':
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
            cur = db.cursor()
                cur.execute("SELECT * FROM `states` WHERE name LIKE 'N%' ")
                print(state) for state in cur.fetchall()
