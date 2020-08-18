#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py) that
    distributes an archive to your web servers,
    using the function do_deploy """
import os
from fabric.api import *


env.hosts = ['35.237.26.128', '3.92.66.113']


def do_deploy(archive_path):
    """ distributes an archive to the
        web server """
    if os.path.exists(archive_path) is False:
        return False
    try:
        arc = archive_path.split('/')[-1]
        path = '/data/web_static/releases'
        directory = arc.split('.')
        put("{}".format(archive_path), "/tmp/{}".format(arc))
        run("sudo mkdir -p {}/{}/".format(path, directory[0]))
        run("sudo tar -xzf /tmp/{} -C {}/{}/".format(arc, path, directory[0]))
        run("sudo rm /tmp/{}".format(arc))
        run("sudo mv {}/{}/web_static/* {}/{}/\
            ".format(path, directory[0], path, directory[0]))
        run("sudo rm -rf {}/{}/web_static".format(path, directory[0]))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {}/{}/ /data/web_static/current\
            ".format(path, directory[0]))
        print('New version deployed!')
        return True
    except Exception:
        return False
