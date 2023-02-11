import pty
from invoke import task


@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def start(ctx):
    ctx.run("p", pty=True)
    
@task
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)


@task
def lint(ctx):
    ctx.run("pylint src", pty=True)
