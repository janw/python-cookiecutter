import subprocess

if "{{cookiecutter.run_git_init}}" == "yes":
    subprocess.run(["git", "init", "."])
if "{{cookiecutter.run_poetry_install}}" == "yes":
    subprocess.run(["poetry", "--no-interaction", "install"])
if "{{cookiecutter.run_precommit_install}}" == "yes":
    subprocess.run(["pre-commit", "install", "-t", "pre-commit"])
    subprocess.run(["pre-commit", "install", "-t", "pre-push"])
