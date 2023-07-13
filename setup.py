from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in overwatch/__init__.py
from overwatch import __version__ as version

setup(
	name="overwatch",
	version=version,
	description="Overwatch",
	author="Flexcom Systems",
	author_email="info@flexcomsystems.net",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
