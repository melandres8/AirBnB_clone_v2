#!/usr/bin/python3
""" Compress before sending """
from datetime import datetime
from fabric.api import local


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
