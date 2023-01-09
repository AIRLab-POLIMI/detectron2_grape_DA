"""To Install requirements in Docker container TODO: customise docker image"""
import subprocess
import sys
import distutils
import os

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])


dist = distutils.core.run_setup("./setup.py")
for x in dist.install_requires:
    install(x)

sys.path.insert(0, os.path.abspath('./detectron2'))
