from setuptools import setup, find_packages

setup(
    name="ipv6-ftp-server",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"}
)