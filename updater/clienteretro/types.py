#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
'''
   ClienteRetro library

'''

class Game(object):
    def __init__(self, game_info={}):
        assert(isinstance(game_info, dict))
        self.id = game_info['id']
        self.name = game_info['nombre']
        self.screens_caps = game_info.get('capturas', [])
        self.cover = game_info.get('caratula', None)
        self.command = game_info.get('comando', u'')
        self.description = game_info.get('descripcion', u'')
        self.developer = game_info.get('programador')
        self.developer_id = game_info['idProgramador']
        self.distributor = game_info.get('distribuidor', u'')
        self.distributor_id = game_info['idDistribuidor']
        self.download_link = game_info.get('enlaceDescarga', None)
        self.youtube = game_info.get('enlaceYoutube', None)
        self.genre = game_info.get('genero', None)
        self.genre_id = game_info['idGenero']
        self.extras = game_info.get('materialExtra', u'')
        self.thumbnail = game_info.get('miniatura', None)
        self.score = game_info.get('puntuacion', u'')
        self.system = game_info.get('sistema', None)
        self.system_id = game_info['idSistema']
        self.rom = game_info.get('rom', u'')

    def __str__(self):
        minidesc = u'Juego "%s" (#%s) por %s' % (self.name,
                                                 self.id,
                                                 self.developer)
        return minidesc.encode('utf-8')
        

class Developer(object):
    def __init__(self, developer_info={}):
        assert(isinstance(developer_info, dict))
        self.id = developer_info['identificador']
        self.logo = developer_info.get('imagen', None)
        self.name = developer_info.get('nombre', u'')
        self.description = developer_info.get('descripcion', u'')

    def __str__(self):
        minidesc = u'Programador "%s" (#%s)' % (self.name, self.id)
        return minidesc.encode('utf-8')


class System(object):
    def __init__(self, system_info={}):
        assert(isinstance(system_info, dict))
        self.id = system_info['id']
        self.name = system_info.get('nombre', '')
        self.description = system_info.get('descripcion', '')
        self.manufacturer = system_info.get('fabricante', '')
        self.manufacturer_id = system_info['idFabricante']
        self.year = system_info['anio']

    def __str__(self):
        minidesc = u'Sistema "%s" (#%s) fabricado por %s' % (self.name,
                                                             self.id,
                                                             self.manufacturer)
        return minidesc.encode('utf-8')


class Genre(object):
    def __init__(self, genre_info={}):
        assert(isinstance(genre_info, dict))
        self.id = genre_info['id']
        self.name = genre_info.get('nombre', '')
        self.description = genre_info.get('descripcion', '')

    def __str__(self):
        minidesc = u'Genero "%s" (#%s)' % (self.name, self.id)
        return minidesc.encode('utf-8')

