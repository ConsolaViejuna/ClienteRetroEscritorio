#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
'''
   ClienteRetro libreria de tipos

'''


def __eq__(obj1, obj2):
    '''Compara los atributos publicos de dos objetos'''
    if type(obj1) != type(obj2):
        return False
    attributes = filter((
        lambda attr: (not attr.startswith('__') and
                      not attr.endswith('__'))), obj1.__dict__.keys())
    for attribute in attributes:
        if getattr(obj1, attribute) != getattr(obj2, attribute):
            return False
    return True

    
class Juego(object):
    id = None
    nombre = None
    capturas = []
    caratula = None
    comando = ''
    descripcion = ''
    programador = ''
    idProgramador = None
    distribuidor = ''
    idDistribuidor = None
    enlaceDescarga = None
    enlaceYoutube = None
    genero = None
    idGenero = None
    materialExtra = ''
    miniatura = None
    puntuacion = ''
    sistema = None
    idSistema = None
    rom = ''
    def __init__(self, info={}):
        assert(isinstance(info, dict))
        self.id = info['id']
        self.nombre = info['nombre']
        self.capturas = info.get('capturas', [])
        self.caratula = info.get('caratula', None)
        self.comando = info.get('comando', u'')
        self.descripcion = info.get('descripcion', u'')
        self.programador = info['programador']
        self.idProgramador = info['idProgramador']
        self.distribuidor = info.get('distribuidor', u'')
        self.idDistribuidor = info['idDistribuidor']
        self.enlaceDescarga = info.get('enlaceDescarga', None)
        self.enlaceYoutube = info.get('enlaceYoutube', None)
        self.genero = info.get('genero', None)
        self.idGenero = info['idGenero']
        self.materialExtra = info.get('materialExtra', u'')
        self.miniatura = info.get('miniatura', None)
        self.puntuacion = info.get('puntuacion', u'')
        self.sistema = info.get('sistema', None)
        self.idSistema = info['idSistema']
        self.rom = info.get('rom', u'')

    def __eq__(self, other_game):
        return __eq__(self, other_game)

    def __ne__(self, other_game):
        return not __eq__(self, other_game)
        
    def __str__(self):
        minidesc = u'Juego "%s" (#%s) por %s' % (self.nombre,
                                                 self.id,
                                                 self.programador)
        return minidesc.encode('utf-8')
        

class Programador(object):
    identificador = None
    imagen = None
    nombre = ''
    descripcion = ''
    def __init__(self, info={}):
        assert(isinstance(info, dict))
        self.identificador = info['identificador']
        self.imagen = info.get('imagen', None)
        self.nombre = info.get('nombre', u'')
        self.descripcion = info.get('descripcion', u'')

    def __eq__(self, other_developer):
        return __eq__(self, other_developer)

    def __ne__(self, other_developer):
        return not __eq__(self, other_developer)

    def __str__(self):
        minidesc = u'Programador "%s" (#%s)' % (self.nombre,
                                                self.identificador)
        return minidesc.encode('utf-8')


class Sistema(object):
    id = None
    nombre = ''
    descripcion = ''
    fabricante = ''
    idFabricante = ''
    anio = ''
    def __init__(self, info={}):
        assert(isinstance(info, dict))
        self.id = info['id']
        self.nombre = info.get('nombre', '')
        self.descripcion = info.get('descripcion', '')
        self.fabricante = info.get('fabricante', '')
        self.idFabricante = info['idFabricante']
        self.anio = info['anio']

    def __eq__(self, other_system):
        return __eq__(self, other_system)

    def __ne__(self, other_system):
        return not __eq__(self, other_system)

    def __str__(self):
        minidesc = u'Sistema "%s" (#%s) fabricado por %s' % (self.nombre,
                                                             self.id,
                                                             self.fabricante)
        return minidesc.encode('utf-8')


class Genero(object):
    id = None
    nombre = ''
    descripcion = ''
    def __init__(self, info={}):
        assert(isinstance(info, dict))
        self.id = info['id']
        self.nombre = info.get('nombre', '')
        self.descripcion = info.get('descripcion', '')

    def __eq__(self, other_genre):
        return __eq__(self, other_genre)

    def __ne__(self, other_system):
        return not __eq__(self, other_genre)

    def __str__(self):
        minidesc = u'Genero "%s" (#%s)' % (self.nombre, self.id)
        return minidesc.encode('utf-8')
