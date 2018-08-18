from setuptools import setup, find_packages
import os

base_dir = os.path.dirname(__file__)

__author__ = "kyhau"
__email__ = "virtualda@gmail.com"

__title__ = "bc_simple"
__version__ = "0.1.0"
__summary__ = "This package includes some simple scripts for setting up local development environment."
__uri__ = "https://github.com/kyhau/arki"

__requirements__ = [
#    "boto3==1.7.50",
]

setup(
    name=__title__,
    version=__version__,
    description=__summary__,
    packages=find_packages(exclude=["tests"]),
    author=__author__,
    author_email=__email__,
    url=__uri__,
    zip_safe=False,
    install_requires=__requirements__,
)
