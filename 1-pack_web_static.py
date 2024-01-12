#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo"""

from fabric.api import local
import time


def do_pack():
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except Exception as e:
        return None
