#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Visita https://github.com/ConsolaViejuna/ClienteRetroEscritorio
# para mas informacion sobre el proyecto
#

from setuptools import setup

setup(name='retroupdater',
      version='0.1',
      description='Cliente para actualizar los datos de ClienteRetro',
      url='https://github.com/ConsolaViejuna/ClienteRetroEscritorio',
      author='Int-0',
      author_email='tobias.deb@gmail.com',
      license='GPL v3.0',
      packages=['clienteretro'],
      package_dir={'clienteretro': 'clienteretro'},
      zip_safe=False)
