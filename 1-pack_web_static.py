#!/usr/bin/python3
from fabric.api import local
from time import strftime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder
    of the AirBnB Clone repo"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(
            strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(
            strftime("%Y%m%d%H%M%S")))
    except Exception as e:
        return None
