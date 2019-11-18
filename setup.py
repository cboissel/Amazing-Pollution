#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 13:37:13 2019

@author: boisselcamille
"""

import os
from distutils.core import setup
from setuptools import find_packages

here = os.path.dirname(__file__)
packages = find_packages(where=here)
package_dir = {k: os.path.join(here, k.replace(".", "/")) for k in packages}

with open(os.path.join(here, "requirements.txt"), "r") as f:
    requirements = f.read().split("\n")

setup(name='ensae2019',
      version='0.1',
      description="Example of module to share plotting functions",
      long_description="Exemple de module python pour partager ses graphes.",
      author='Boissel Camille, Cazanave Thibaud, Cerles Sébastien, Chabriel Maxime, Fourchault Raphaël',
      url='https://github.com/cboissel/Amazing-Pollution/blob/master/setup.py',
      packages=packages,
      package_dir=package_dir,
      # requires indique quels packages doivent être installés
      # également pour que cela fonctionne
      requires=requirements)
