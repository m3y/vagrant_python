#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import run
from fabric.api import cd
from fabric.api import sudo
from fabric.api import env
from fabric.colors import red, green

import cuisine

cuisine.select_package("apt")


def setup():
    _setup_ubuntu()
    _install_dotfiles()
    _install_python3()


def _setup_ubuntu():
    sudo("cp /usr/share/zoneinfo/Japan /etc/localtime")
    sudo("apt-get update")
    cuisine.package_ensure('git')
    cuisine.package_ensure('exuberant-ctags')


def _install_dotfiles():
    env.forward_agent = True
    run("git clone git@github.com:m3y/dotfiles.git")
    with cd("/home/vagrant/dotfiles"):
        run("make install")
    print(green("[dotfiles] installed."))


def _install_python3():
    sudo("add-apt-repository ppa:fkrull/deadsnakes")
    sudo("apt-get update")
    sudo("apt-get install python3.4")
