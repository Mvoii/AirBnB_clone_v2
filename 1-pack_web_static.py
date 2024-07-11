#!/usr/bin/python3
"""
the odule provides a function to create a .tgz archive from web_static folder
"""

from datetime import datetime
from fabric.api import local

def do_pack():
    """
    creates a .tgz archive from the contents of the web_static folder
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    # construct the path to save archive
    archieve_path = "versions/web_static_{}.tgz".format(now)

    #use fabric to create the dir if not exists
    local("mkdir -p versions")

    # create the archive
    archived = local("tar -cvzf {} web_static".format(archieve_path))

    # check archive creation status
    if archived.return_code != 0:
        return None
    else:
        return archieve_path
    # try:
    #     local("mkdir -p versions")
    #     current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    #     file_name = "versions/web_static_{}.tgz".format(current_time)
    #     local("tar -cvzf {} web_static".format(file_name))
    #     return file_name
    # except:
    #     return None
