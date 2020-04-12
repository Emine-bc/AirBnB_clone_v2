#!/usr/bin/python3
'''Fabric script that generates a .tgz archive from the contents
   of Airbnb_clone_v2
'''
from datetime import datetime
from fabric.api import *
from time import strftime


def do_pack():
    """function"""
    local("mkdir -p versions")
    t = strftime("%Y%m%d%H%M%S")
    full = local("tar -cvzf versions/web_static_{}.tgz web_static".format(t))
    if full.succeeded:
        return ("versions/web_static_{}".format(t))
    return (None)
