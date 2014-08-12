# -*- coding: utf-8 -*-
import os
from os.path import join as opj
import subprocess
import sys

class UnmetDependency(OSError):
    pass

class CallError(Exception):
    def __init__(self, *args, **kw):
        returncode = kw.pop('returncode', 1)
        super(CallError, self).__init__(*args, **kw)
        self.returncode = returncode

def call(*args):
    try:
        r = subprocess.check_output(args, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        if e.output:
            raise CallError(e.output.decode('utf8'), returncode=e.returncode)
        raise e
    return r.decode('utf8')

def qdiff(left, right):
    left, right = opj(left, ''), opj(right, '')
    os.chdir(left)
    call('bzr', 'init', '-q')
    call('bzr', 'add', '-q')
    # Set dummy identity in case bzr is not configured
    call('bzr', 'whoami', '-d', '.', '"Your Name <name@example.com>"')
    call('bzr', 'commit', '-qmm')
    call('rsync', '-qavLt', '--delete', '--exclude=/.bzr', right, left)
    call('bzr', 'add', '-q')
    call('bzr', 'qdiff', '-q')

def check_dependencies():
    try:
        gitv = call('git', '--version').split()[2]
    except CallError:
        raise UnmetDependency("Could not find `git` program")

    ver = list(map(int, gitv.split('.')[0:3]))
    if ver < [1, 7, 11]:
        raise UnmetDependency("Need at least `git` version 1.7.11+")

    try:
        call('bzr', 'version').splitlines()[0].split()[-1]
    except CallError:
        raise UnmetDependency("Could not find `bzr` program")

    try:
        call('bzr', 'qdiff', '--help')
    except CallError:
        raise UnmetDependency("Could not find `bzr qdiff` plugin")

    try:
        call('rsync', '--help')
    except CallError:
        raise UnmetDependency("Could not find `rsync` program")

def main():
    try:
        check_dependencies()
    except Exception as e:
        sys.exit(str(e))
    if len(sys.argv) == 3:
        left, right = sys.argv[1:3]
        if os.path.isdir(left) and os.path.isdir(right):
            try:
                qdiff(left, right)
            except Exception as e:
                sys.exit(str(e))
            sys.exit(0)

    # TODO: ensure infinite subcalls is not possible
    cmd = ['git', 'difftool', '-d', '-x'] + sys.argv
    # print("Launching '%s'" % ' '.join(cmd))
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError as e:
        sys.stderr.write(str(e))
        sys.exit(e.returncode)
