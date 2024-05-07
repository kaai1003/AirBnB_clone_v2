#!/usr/bin/python3
"""compress web_static to tgz file"""
from fabric import run, cd
from datetime import datetime


def do_pack():
    """tgz file creation"""
    src_folder = "./web_static"
    out_folder = "./versions"
    creation_dt = datetime.now().strftime("%Y%md%H%M%S")
    run("mkdir -p {}".format(out_folder))
    with cd(src_folder):
        run("tar -czvf {}/web_static_{}.tgz .".format(out_folder, creation_dt))


do_pack()
