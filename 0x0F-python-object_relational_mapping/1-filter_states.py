#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    dtbs = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], dtbs=sys.argv[3])
    c = dtbs.cursor()
    c.execute("SELECT * FROM `state` ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
