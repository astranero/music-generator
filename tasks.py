import pty
from invoke import task
import time

@task
def test(ctx):
    ctx.run("poetry run pytest src", pty=True)


@task
def start(ctx):
    ctx.run("poetry run python src/main.py", pty=True)


@task
def coverage_report(ctx):
    ctx.run("poetry run pytest --cov-report html --cov=src", pty=True)
    ctx.run("chmod u+x trigger_push_htmlcov.sh", pty=True)
    ctx.run("bash trigger_push_htmlcov.sh", pty=True)
    time.sleep(2)


@task
def push(ctx, msg):
    ctx.run("git add .", pty=True)
    ctx.run(f"git commit -m {msg}")
    ctx.run("git push origin main", pty=True)
    coverage_report(ctx)


@task
def lint(ctx):
    ctx.run("pylint src", pty=True)
