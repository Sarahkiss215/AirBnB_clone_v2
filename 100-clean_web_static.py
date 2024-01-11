#!/usr/bin/python3
"""Deletes out-of-date archives, using the function do_clean"""
import os
from fabric.api import *

env.hosts = ["54.144.149.14", "18.209.179.185"]
env.user = "ubuntu"
env.key_filename = '~/.ssh/0-RSA_key'


def do_clean(number=0):
    """Deletes out-of-date archives
    Args:
        number (int): The number of archives,
                      including the most recent, to keep
    If number is 0 or 1, keep only the most recent version of the archive
    if number is 2, keep the most recent, and second most recent versions
    of the archive
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
