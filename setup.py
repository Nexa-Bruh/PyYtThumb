# Copyright (c) 2021 Itz-fork
# Part of Py-Yt-Thumb Project

import os
from setuptools import setup, find_packages

# Allow Exec. from any path (Credits: mega.py)
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Getting the requirements
with open('requirements.txt') as req:
    reques = req.read().splitlines()


setup(name='PyYtThumb',
version='0.1',
description='A Simple Python Program to Get All Possible Thumbnail Urls From a Youtube Video Link',
url='https://github.com/Itz-fork/Py-yt-Thumb',
author='Itz-fork',
author_email='itz-fork@users.noreply.github.com',
license='MIT',
packages=find_packages('PyYtThumb'),
keywords=['python', 'youtube'],
install_requires=reques,
classifiers= [
            "Programming Language :: Python :: 3"
            "License :: OSI Approved :: MIT License"
            "Operating System :: OS Independent"
        ])