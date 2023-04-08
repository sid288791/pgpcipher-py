from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='pgpcipher-py',
   version='1.0',
   description='A useful module for pgp',
   license="MIT",
   long_description=long_description,
   author='Siddharth',
   author_email='siddharth@openPGP.com',
   url="",
   packages=['openPGP'],  #same as name
   install_requires=['python-gnupg'], #external packages as dependencies
)