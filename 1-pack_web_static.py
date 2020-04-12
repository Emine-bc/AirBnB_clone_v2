#!/usr/bin/python3
'''Fabric script that generates a .tgz archive from the contents
   of Airbnb_clone_v2
'''
from datetime import datetime
from fabric.api import *


def do_pack():
    """function"""
    local("mkdir -p versions")
    full = local("tar -cvzf versions/web_static_{}.tgz\
        web_static".format(strftime("%Y%m%d%H%M%S")))
    if full:
        return ("versions/web_static_{}".format(strftime("%Y%m%d%H%M%S")))
    return (None)
