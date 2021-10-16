# -*- coding: utf-8 -*-
# @File     : setup.py
# @Time     : 2021/10/16 11:18
# @Author   : Jckling

import setuptools


setuptools.setup(
    name="dailycheckin",
    version="0.0.1",
    author="Jckling",
    description="基于 dailycheckin 修改的签到工具",
    url="https://github.com/jckling/Daily-Bonus",
    install_requires=[
        'beautifulsoup4',
        'cryptography',
        'lxml',
        'requests',
        'urllib3'
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Natural Language :: Chinese (Simplified)",
    ],
    package_dir={"dailycheckin": "dailycheckin"},
    packages=setuptools.find_packages(),
)
