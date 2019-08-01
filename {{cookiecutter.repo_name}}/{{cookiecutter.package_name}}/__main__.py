import sys

from {{cookiecutter.package_name}}.base import fib


def main(args):
    if len(args) > 0:
        print(fib(int(args[0])))
        return
    raise Exception("Input argument expected.")


main(sys.argv[1:])
