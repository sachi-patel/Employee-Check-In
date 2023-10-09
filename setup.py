from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in empcheck/__init__.py
from empcheck import __version__ as version

setup(
	name="empcheck",
	version=version,
	description="empcheck",
	author="empcheck",
	author_email="empcheck",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
