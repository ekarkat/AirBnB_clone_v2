#!/usr/bin/python3
# Fabric do_deploy
from fabric.api import put, env, run

env.hosts = ["35.153.93.177", "34.203.77.10"]

def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    try:
        file = file = archive_path.split("/")[-1].split(".")[0]
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
        con.run("ln -sf {}/{} /data/web_static/current".format(pat, file))
        return True
    except Exception:
        return False
