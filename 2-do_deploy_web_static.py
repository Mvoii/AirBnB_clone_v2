#!/usr/bin/python3
"""
the fab distributes an archive to my webservers
"""

import os
from fabric.api import *
from datetime import datetime

# set the host IPs for web-01 and web-02 
env.hosts = ['100.25.165.200', '52.207.85.124']
env.user = "ubuntu"

def do_pack():
    """function to compress web_static folder"""
    # obtaion the current time
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    # construct the file path
    archived_path = "versions/web_static_{}.tgz".format(now)

    # create the folder if it does not exist
    local("mkdir -p versions")

    # compress the folder
    archived = local("tar -cvzf {} web_static".format(archived_path))

    # check archive creation status
    if archived.return_code != 0:
        return None
    else:
        return archived_path
    # try:
    #     if not os.path.exists("versions"):
    #         local("mkdir versions")
    #     date = datetime.now().strftime("%Y%m%d%H%M%S")
    #     file_name = "versions/web_static_{}.tgz".format(date)
    #     local("tar -cvzf {} web_static".format(file_name))
    #     return file_name
    # except:
    #     return None

def do_deploy(archive_path):
    """use os modules to check if file exists"""
    if os.path.exists(archive_path):
        archive = archive_path.split("/")[1]
        a_path = "/tmp/{}".format(archive)
        folder = archive.split(".")[0]
        f_path = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, a_path)
        run("mkdir -p {}".format(f_path))
        run("tar -xzf {} -C {}".format(a_path, f_path))
        run("rm {}".format(a_path))
        run("mv -f {}web_static/* {}".format(f_path, f_path))
        run("rm -rf {}web_static".format(f_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(f_path))
        return True
    return False
