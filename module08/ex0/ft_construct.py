import sys
import site
import os

def main():
    """ Check if you are in a VE"""
    if sys.prefix == sys.base_prefix:
        message = f"""MATRIX STATUS: You're still plugged in

Current Python: {sys.executable}
Virtual Environment: None detected

WARNING: You're in the global environment!
The machines can see everything you install.

To enter the construct, run:
python3 -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env
Scripts
activate # On Windows

Then run this program again.
"""
        print(message)
    else:
        path_instal = site.getsitepackages()
        message_VE = f"""
MATRIX STATUS: Welcome to the construct

Current Python: {sys.executable}
Virtual Environment: {os.path.basename(sys.prefix)}
Environment Path: {sys.exec_prefix}

SUCCESS: You're in an isolated environment!

Safe to install packages without affecting
the global system.

Package installation path:
{path_instal[0]}
"""
        print(message_VE)


if __name__ == "__main__":
    main()
