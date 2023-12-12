#!/usr/bin/python3
'''Compress a directory ro .tgz'''

from datetime import datetime
from fabric import Connection
from invoke import run as local
from fabric import task

con1 = Connection("alx1")
con2 = Connection("alx2")

connections = [con1, con2]

file = "web_static_20231210235730"

for con in connections:
    print("server : {}".format(con.host))
    # transfer the file to tmp
    pat = "/data/web_static/releases/"
    print("ls directory")
    files = con.run("ls {} | grep web_static_ | sort -tr".format(pat), hide=True)
    print(files.stdout)

    # print("Movinf file")
    # con.put("localy.py", "/home/ubuntu")

