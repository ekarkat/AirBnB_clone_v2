#!/usr/bin/python3
'''Compress a directory ro .tgz'''

from datetime import datetime
from fabric.api import local

@task
def do_pack():
    """Create a tgz archive for web_static."""
    date = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}".format(date.year,
                                                     date.month,
                                                     date.day,
                                                     date.hour,
                                                     date.minute,
                                                     date.second)

    local("mkdir -p versions")
    try:
        local("tar -cvzf {}.tgz web_static".format(file))
        return (file)
    except Exception:
        return (None)

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

def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
