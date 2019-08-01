import re
import sys

MODULE_REGEX = r"^[a-zA-Z][_a-zA-Z0-9]+$"
module_name = "{{ cookiecutter.package_name }}"

if not re.match(MODULE_REGEX, module_name):
    print("ERROR: %s is not a valid Python module name!" % module_name)
    sys.exit(1)

VERSION_REGEX = r"^3\.\d+$"
python_version = "{{ cookiecutter.python_version }}"

if not re.match(VERSION_REGEX, python_version):
    print(
        "ERROR: %s is not a valid Python version "
        "(must be '3.<MINOR>', no bugfix version)." % python_version
    )
    sys.exit(1)
