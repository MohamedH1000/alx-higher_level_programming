#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    dtbs = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], dtbs=sys.argv[3])
    c = dtbs.cursor()
    c.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    [print(state) for state in c.fetchall()]
