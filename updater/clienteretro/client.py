#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
'''
   ClienteRetro library

'''

import json
import urllib
import httplib

import clienteretro.types as types

_DEFAULT_URL_ = 'http://clienteretro.consolaviejuna.com/controlador'

# La API REST utiliza varios controladores, aqui definimos todos por defecto
_CONTROLLERS_ = {
    'developers': 'programadorControlador.php',
    'systems': 'sistemaControlador.php',
    'genres': 'generoControlador.php',
    'games': 'juegoControlador.php'
    }

# HTTP headers que mandamos al servidor
_BASE_HEADERS_ = {
    'Content-type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json'
}

# Requests
_CARGAR_SISTEMAS_ = urllib.urlencode({'accion': 'cargar'})
# Muchas requests son iguales pero cambia el controller ;)
_CARGAR_PROGRAMADORES_ = _CARGAR_SISTEMAS_
_CARGAR_GENEROS_ = _CARGAR_SISTEMAS_
_CARGAR_JUEGOS_ = _CARGAR_GENEROS_

def _split_url_(url):
    '''
    Extrae el nombre de maquina de una URL y la ruta

    Ej: "http://maquina.com/ruta" -->  ("maquina.com", "ruta")

    '''
    # Quitamos protocolo si lo hubiera
    if url.startswith('http://'):
        url = url[7:]
    elif url.startswith('https://'):
        # FIXME: Se pretende utilizar https pero por ahora eso
        # no se soporta asi que se ignora y se usa http normal
        # se deberia avisar al usuario pero por ahora no... :P
        url = url[8:]
    else:
        # No reconocemos una URL normal asi que asumimos que es un
        # nombre de maquina listo
        pass

    # Quitamos ruta si la hubiera
    if '/' in url:
        host = url[:url.index('/')]
        address = url[url.index('/'):]
        # Quitamos el '/' final si hubiera
        if address.endswith('/'):
            address = address[:-1]
    else:
        host = url
        address = ''
    return (host, address)


class ObjectNotFound(Exception):
    def __init__(self, element='unknown'):
        self.__element = element

    def __str__(self):
        return 'Element not found in database: %s' % self.__element


class Client(object):
    '''
    Abstraccion de la API REST de clienteRetro
    '''
    def __init__(self, base_url=_DEFAULT_URL_, controllers=_CONTROLLERS_):
        # Verificar diccionario de controladores
        for key in _CONTROLLERS_.keys():
            if key not in controllers.keys():
                raise ValueError('Falta definicion de controlador "%s"' % key)

        self.__host, self.__base = _split_url_(base_url)
        self.__controllers = controllers

        self.__http = httplib.HTTPConnection(self.__host)

        # WRN: La cache no caduca por ahora!
        self.__systems_data = None
        self.__developers_data = None
        self.__genres_data = None
        self.__games_data = {}

    def _controller_address_(self, controller_id):
        assert(controller_id in _CONTROLLERS_.keys())
        return '%s/%s' % (self.__base, self.__controllers[controller_id])

    def _request_(self, request, controller_id):
        self.__http.request('POST',
                            self._controller_address_(controller_id),
                            request,
                            _BASE_HEADERS_)
        result = self.__http.getresponse()
        return result.read()

    @property
    def systems_data(self):
        '''
        Obtiene TODA la informacion sobre los sistemas
        '''
        if self.__systems_data is None:
            self.__systems_data = json.loads(
                self._request_(_CARGAR_SISTEMAS_, 'systems'))
        return self.__systems_data

    @property
    def developers_data(self):
        '''
        Obtiene TODA la informacion sobre los desarrolladores
        '''
        if self.__developers_data is None:
            self.__developers_data = json.loads(
                self._request_(_CARGAR_PROGRAMADORES_, 'developers'))
        return self.__developers_data

    @property
    def genres_data(self):
        '''
        Obtiene TODA la informacion sobre los generos
        '''
        if self.__genres_data is None:
            self.__genres_data = json.loads(
                self._request_(_CARGAR_GENEROS_, 'genres'))
        return self.__genres_data
    
    @property
    def systems_names(self):
        '''
        Obtiene los nombres de todos los sistemas
        '''
        return [system['nombre'] for system in self.systems_data]

    @property
    def systems_ids(self):
        '''
        Obtiene los IDs de todos los sistemas
        '''
        return [system['id'] for system in self.systems_data]

    def get_system(self, system_id):
        '''
        Obtiene la informacion de un sistema concreto
        '''
        if system_id in self.systems_ids:
            # Busqueda por ID
            for system in self.systems_data:
                if system['id'] == system_id:
                    return types.System(system)
        elif system_id in self.systems_names:
            # Busqueda por NOMBRE
            for system in self.systems_data:
                if system['nombre'] == system_id:
                    return types.System(system)
        else:
            raise ObjectNotFound('System %s' % system_id)

    @property
    def developers_names(self):
        '''
        Obtiene los nombres de todos los desarrolladores
        '''
        return [developer['nombre'] for developer in self.developers_data]

    @property
    def developers_ids(self):
        '''
        Obtiene los IDs de todos los desarrolladores
        '''
        return [
            developer['identificador'] for developer in self.developers_data
        ]

    def get_developer(self, developer_id):
        '''
        Obtiene la informacion de un programador concreto
        '''
        if developer_id in self.developers_ids:
            # Busqueda por ID
            for developer in self.developers_data:
                if developer['identificador'] == developer_id:
                    return types.Developer(developer)
        elif developer_id in self.developers_names:
            # Busqueda por NOMBRE
            for developer in self.developers_data:
                if developer['nombre'] == developer_id:
                    return types.Developer(developer)
        raise ObjectNotFound('Developer %s' % developer_id)
        
    @property
    def genres_data(self):
        '''
        Obtiene TODA la informacion sobre los generos
        '''
        if self.__genres_data is None:
            self.__genres_data = json.loads(
                self._request_(_CARGAR_GENEROS_, 'genres'))
        return self.__genres_data
    
    @property
    def genre_names(self):
        '''
        Obtiene los nombres de todos los generos
        '''
        return [genre['nombre'] for genre in self.genres_data]

    @property
    def genre_ids(self):
        '''
        Obtiene los IDs de todos los generos
        '''
        return [genre['id'] for genre in self.genres_data]

    def get_genre(self, genre_id):
        '''
        Obtiene la informacion de un genero concreto
        '''
        if genre_id in self.genre_ids:
            # Busqueda por ID
            for genre in self.genres_data:
                if genre['id'] == genre_id:
                    return types.Genre(genre)
        elif genre_id in self.genre_names:
            # Busqueda por NOMBRE
            for genre in self.genres_data:
                if genre['nombre'] == genre_id:
                    return types.Genre(genre)
        else:
            raise ObjectNotFound('Genre %s' % genre_id)

    def get_games_of(self, developer_id):
        '''
        Obtiene TODA la informacion sobre los juegos de un programador
        '''
        # FIX: el diccionario almacena un programador
        assert(developer_id is not None)        
        if self.__games_data.get(developer_id, None) is None:
            if developer_id not in self.developers_ids:
                developer_id = self.get_developer(developer_id)['identificador']
                print developer_id
            result = self._request_(
                urllib.urlencode({'accion': 'cargarPorId',
                                  'id': developer_id}), 'games')
            self.__games_data[developer_id] = json.loads(result)
        return [types.Game(data) for data in self.__games_data[developer_id]]
