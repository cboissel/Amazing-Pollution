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

setup(name='td2a_plotting',
      version='0.1',
      description="Example of module to share plotting functions",
      long_description="Exemple de module python pour partager ses graphes.",
      author='Boissel Camille, Cazanave Thibaud, Cerles Sébastien, Chabriel Maxime, Fourchault Raphaël',
      url='https://github.com/SebastienCerles/Amazing-Pollution?fbclid=IwAR2HhOJPM4McsnxmZU0uF3PGVsx1l4ZSe9wTO2goPJaOtrSsE27Lj7LA5nY',
      packages=packages,
      package_dir=package_dir,
      # requires indique quels packages doivent être installés
      # également pour que cela fonctionne
      requires=requirements)