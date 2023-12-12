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
    files = local("ls versions | grep web_static_ | sort -tr")
    files_list = files.stdout.split("\n")
    while len(files_list) > number:
        if files_list[-1] == "":
            files_list.pop()
        else:
            local("rm versions/{}".format(files_list.pop()))
    # remotely:
    pat = "/data/web_static/releases"
    files = run("ls versions | grep web_static_ | sort -tr")
    files_list = files.split("\n")
    while len(files_list) > number:
        if files_list[-1] == "":
            files_list.pop()
        else:
            run("rm {}/{}".format(pat, files_list.pop()))
