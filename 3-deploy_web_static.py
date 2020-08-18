#!/usr/bin/python3
""" Full deployment web static """
import os
from fabric.api import *
from datetime import datetime


env.hosts = ['35.237.26.128', '3.92.66.113']
path = None


def do_pack():
    """ Generate the archive .tgz """
    ftime = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    fname = "versions/web_static_{}.tgz".format(ftime)

    if fname:
        local('sudo mkdir -p ./versions')
        local('tar -cvzf {} ./web_static'.format(fname))
        return fname
    else:
        return None


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


def deploy():
    """ script (based on the file 2-do_deploy_web_static.py) that creates
        and distributes an archive to your web servers,
        using the function deploy """
    global path

    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
