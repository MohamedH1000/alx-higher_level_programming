#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    dtbs = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], dtbs=sys.argv[3])
    c = dtbs.cursor()
    c.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))
