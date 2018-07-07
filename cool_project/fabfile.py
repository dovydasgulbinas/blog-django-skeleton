import os
from invoke import task

# These constants are Hacky, but for now I do not know how to fix it using
# invoke, because invoke does not load exported variables of my terminal session
AC = 'export TERM=xterm-256color; source ../env/bin/activate'
ACA = AC + ' && '



@task
def penv(c):
    c.run(ACA + "/usr/bin/env", pty=True)


@task
def freeze(c):
    output = c.run(ACA + "pip freeze > requirements.txt")


@task
def shellbp(c):
    c.run(ACA + 'bpython -i manage.py shell', pty=True)


@task
def shell(c):
    c.run(ACA + 'manage.py shell', pty=True)


@task
def run(c):
    c.run(ACA + 'manage.py runserver', pty=True)


@task
def purge_cache(c):
    c.run(ACA + 'find . -d -name __pycache__ -exec rm -rf {} \;', pty=True)


@task
def test(c):
    c.run(ACA + 'manage.py test', pty=True)

