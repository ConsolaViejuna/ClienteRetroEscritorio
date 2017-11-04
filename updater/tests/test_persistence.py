#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

'''
Test sencillos para la libreria de acceso a la API REST
'''

import clienteretro.types
import clienteretro.persistence

db = clienteretro.persistence.DataBase()
db.create_table_for_class(clienteretro.types.Genero)

genre = clienteretro.types.Genero({'id': 'hola'})
db.save_object(genre)
genre = db.get_object(clienteretro.types.Genero, id='hola')
print 'Initial:', genre

genre.nombre = 'Tontaco'
db.update_object(genre)
print 'Updated:', genre

genre = db.get_object(clienteretro.types.Genero, id='hola')
print 'Restored:', genre
