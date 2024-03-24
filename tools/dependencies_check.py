# FMAP
# A audio file format that takes in frequency values or notes and turns them into WAV format.
# GitHub: https://www.gitub.com/lewisevans2007/FMAP
# Licence: GNU General Public Licence v3.0
# By: Lewis Evans
#
# This script checks if all the dependencies are installed.

import sys

RED = "\033[91m"
GREEN = "\033[92m"

TICK = GREEN + "✓" + "\033[0m"
CROSS = RED + "✗" + "\033[0m"
TRIANGLE = RED + "▲" + "\033[0m"

not_installed = []

try:
    import numpy
    print(f"{TICK} numpy")
except ImportError:
    print(f"{CROSS} numpy")
    not_installed.append("numpy")

try:
    import setuptools
    print(f"{TICK} setuptools")
except ImportError:
    print(f"{CROSS} setuptools")
    not_installed.append("setuptools")

if len(not_installed) > 0:
    print(f"\n{TRIANGLE} Missing dependencies found.")
    print(f"Please run make install_requirements to install the missing dependencies.")
    sys.exit(1)
else:
    print(f"\n{GREEN}All dependencies are installed.\033[0m")
    sys.exit(0)