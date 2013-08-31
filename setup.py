#!/usr/bin/env python3
# rpcalc setup script
# for more info, see github.com/qguv/rpcalc

from distutils.core import setup

setup(  name = "rpcalc",
        version = "0.4",
        description = "A reverse polish notation calculator written in Python 3.",
        author = "Quint Guvernator",
        author_email = "quintus.public@gmail.com",
        url = "https://github.com/qguv/rpcalc",
        package_dir = {"rpcalc":"src"},
        packages = ["rpcalc"]
     )
