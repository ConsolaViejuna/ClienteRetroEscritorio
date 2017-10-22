#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

'''
Test sencillos para la libreria de acceso a la API REST
'''

import clienteretro

cliente_retro = clienteretro.Client()
print cliente_retro.systems_names
print cliente_retro.systems_ids
print cliente_retro.genre_ids
print cliente_retro.get_genre('3')
print cliente_retro.get_system('7')
print cliente_retro.developers_names
print cliente_retro.developers_ids
print cliente_retro.get_developer('mojontwins')
for game in cliente_retro.get_games_of('mojontwins'):
    print game
