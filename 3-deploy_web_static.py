#!/usr/bin/python3
""" Full deployment web static """
import os
from fabric.api import *
from datetime import datetime


do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ['35.237.26.128', '3.92.66.113']
path = ''


def deploy():
    """ script (based on the file 2-do_deploy_web_static.py) that creates
        and distributes an archive to your web servers,
        using the function deploy """
    global path
    if not path:
        path = do_pack()
    if not path:
        return False
    return do_deploy(path)
