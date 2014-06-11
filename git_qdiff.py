#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from os.path import join as opj
import subprocess
import sys

class UnmetDependency(OSError):
    pass

def qdiff(left, right):
    left, right = opj(left, ''), opj(right, '')
    os.chdir(left)
    subprocess.check_call(['bzr', 'init', '-q'])
    subprocess.check_call(['bzr', 'add', '-q'])
    subprocess.check_call(['bzr', 'commit', '-qmm'])
    subprocess.check_call(['rsync', '-qavLt', '--delete', '--exclude=/.bzr', right, left])
    subprocess.check_call(['bzr', 'add', '-q'])
    subprocess.check_call(['bzr', 'qdiff', '-q'])

def check_dependencies():
    try:
        gitv = subprocess.check_output(['git', '--version']).split()[-1]
    except subprocess.CalledProcessError:
        raise UnmetDependency("Could not find `git` program")

    ver = map(int, gitv.split('.')[0:3])
    if cmp(ver, [1, 7, 11]) < 0:
        raise UnmetDependency("Need at least `git` version 1.7.11+")

    try:
        bzrv = subprocess.check_output(['bzr', 'version']).splitlines()[0].split()[-1]
    except subprocess.CalledProcessError:
        raise UnmetDependency("Could not find `bzr` program")

    try:
        subprocess.check_output(['bzr', 'qdiff', '--help'])
    except subprocess.CalledProcessError:
        raise UnmetDependency("Could not find `bzr qdiff` plugin")

    return gitv and bzrv # TODO: check minimum requirements

def main():
    try:
        check_dependencies()
    except Exception, e:
        sys.exit(e.message)
    if len(sys.argv) == 3:
        left, right = sys.argv[1:3]
        if os.path.isdir(left) and os.path.isdir(right):
            qdiff(left, right)
            sys.exit(0)

    # TODO: ensure infinite subcalls is not possible
    cmd = ['git', 'difftool', '-d', '-x'] + sys.argv
    # print("Launching '%s'" % ' '.join(cmd))
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError, e:
        sys.exit("git failed with returncode %d" % e.returncode)
