#!/usr/bin/python3
'''Fabric script that generates a .tgz archive from the contents
   of Airbnb_clone_v2
'''

from datetime import datetime
from fabric.api import *
from time import strftime
env.hosts = ["34.73.0.225", "35.229.78.70"]


def do_pack():
    """function"""
    local("mkdir -p versions")
    full = local("tar -cvzf versions/web_static_{}.tgz\
        web_static".format(strftime("%Y%m%d%H%M%S")))
    if full:
        return ("versions/web_static_{}".format(strftime("%Y%m%d%H%M%S")))
    return (None)


def do_deploy(archive_path):
    '''func deploy'''
    if not os.path.exists(archive_path):
        return(False)
    try:
        put(archive_path, "/tmp/")
        deploy_file = archive_path.split("/")[1].split(".")[0]
        file_path = file_deploy.split(".")[0]
        path = archive_path.split("/")[-1]
        deploy_path = "/data/web_static/releases/{}".format(deploy_file)
        run("mkdir -p {}".format(deploy_path))
        run("tar -xzf /tmp/{} - C {}".format(path, deploy_path))
        run("rm -rf /tmp/{}".format(path))
        run("mv {}/web_static/* {}/".format(deploy_path, deploy_path))
        run("rm -rf {}/web_static".format(deploy_path))
        run("rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(deploy_path))
        return(True)
    except:
        return(False)
