#!/usr/bin/python3
# Fabric do_deploy
from fabric.api import put, env, run, task
import re

env.hosts = ["35.153.93.177", "34.203.77.10"]


@task
def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    try:
        file = file = re.search(r'web_static_[0-9]*\.tgz', archive_path)
    except Exception:
        return False
    try:
        pat = "/data/web_static/releases"
        put("versions/{}.tgz".format(file), "/tmp/")
        con.run("mkdir -p {}/{}/".format(pat, file))
        con.run("tar -xzf /tmp/{}.tgz -C {}/{}".format(file, pat, file))
        con.run("rm -f /tmp/{}.tgz".format(file))
        con.run("rm -rf /data/web_static/current")
        con.run("mv {}/{}/web_static/* {}/{}/".format(pat, file, pat, file))
        con.run("rm -rf {}/{}/web_static/".format(pat, file))
        con.run("ln -s {}/{} /data/web_static/current".format(pat, file))
        return True
    except Exception:
        return False
