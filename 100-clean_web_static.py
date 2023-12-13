#!/usr/bin/python3
'''Compress a directory ro .tgz'''

from datetime import datetime
from fabric.api import local
from fabric.api import put, env, run, task
import re

env.hosts = ["35.153.93.177", "34.203.77.10"]


def do_clean(number=0):
    """Clean up old versions"""
    if number == 0:
        number = 1
    # locally:
    with lcd("versions"):
        files = local("ls -tr").split("\n")
        while len(files) > number:
            if files[-1] == "":
                files.pop()
            else:
                local("rm {}".format(files.pop()))
    # remotely:
    pat = "/data/web_static/releases"
    with cd("/data/web_static/releases"):
        files = run("ls -tr").split("\n")
        while len(files) > number:
            if files[-1] == "":
                files.pop()
            else:
                run("rm -rf {}".format(files.pop()))
