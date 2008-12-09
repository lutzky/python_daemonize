#!/usr/bin/python

# daemonize.py by Ohad Lutzky <ohad@lutzky.net>
# Ported from Brian Clapper's daemonize at
# http://www.clapper.org/software/daemonize/

"""Simple daemonization utility based on BSD daemon(3)

Usage from within python:
- import daemonize
- run daemonize.daemon() at the appropriate time

Usage from the shell:
daemonize.py [path] [arguments]

Note that [path] has to be a full path to an executable file
"""

import os, sys

def daemon(nochdir = False, noclose = False):
    """Daemonizes the current process; this means detaching from the
    controlling terminal and running in the background as a system
    daemon.

    Unless nochdir is set, the current working directory is set to "/".

    Unless noclose is set, standard input, output and error will be
    redirected to /dev/null."""

    def do_fork():
        if os.fork() != 0:
            # This is the parent, we should exit
            os._exit(0)
        # Note that we don't check the return value of fork - we want to
        # become a child, and upon error, an exception will be thrown

    def redirect_fds():
        os.close(0)
        os.close(1)
        os.close(2)

        os.open("/dev/null", os.O_RDWR)
        os.dup(0)
        os.dup(0)

    do_fork()
    os.setsid()
    do_fork()
    os.umask(0)

    if not nochdir: os.chdir("/")
    if not noclose: redirect_fds()

if __name__ == '__main__':
    daemon(0,0)
    os.execv(sys.argv[1], sys.argv[2:])
