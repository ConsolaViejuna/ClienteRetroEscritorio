#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
'''
   ClienteRetro library
'''

import sqlite3

def _get_table_and_attrs_(any_object):
    table = any_object.__name__
    attributes = filter(
        (lambda attr: (not attr.startswith('__') and not attr.endswith('__'))),
        any_object.__dict__.keys())
    attributes.sort()
    return table, attributes


class DataBase(object):
    def __init__(self, sql_file=':memory:'):
        self.__db = sqlite3.connect(sql_file)

    def create_table_for_class(self, classobject):
        table, attributes = _get_table_and_attrs_(classobject)
        row_format = ''
        for attribute in attributes:
            row_format += (('%s text,' % attribute) if attribute != 'id' else
                           ('%s text primary key,' % attribute))
        cmd = 'create table if not exists %s (%s)' % (table, row_format[:-1])
        self.__db.execute(cmd)
        self.__db.commit()

    def get_object(self, classobject, id):
        table = classobject.__name__
        obj = self.__db.execute('select * from %s where id=?' % table, (id,))
        column_names = [column[0] for column in obj.description]
        row_values = obj.fetchone()
        if not row_values:
            return
        return classobject(dict(zip(column_names, row_values)))

    def get_all_objects(self, classobject):
        table = classobject.__name__
        objs = self.__db.execute('select * from %s' % table)
        column_names = [column[0] for column in objs.description]
        result = []
        for row_values in objs.fetchall():
            result.append(classobject(dict(zip(column_names, row_values))))
        return result

    def save_object(self, nonpersistent_object):
        stored_object = self.get_object(type(nonpersistent_object),
                                        id=nonpersistent_object.id)
        if stored_object is not None:
            self.update_object(nonpersistent_object)
            return
        table, attributes = _get_table_and_attrs_(
            nonpersistent_object.__class__)
        values = tuple()
        for attr in attributes:
            values += (getattr(nonpersistent_object, attr),)
        cmd = 'insert into %s(%s) values(%s)' % (
            table,
            ','.join(attributes),
            ','.join(['?'] * len(attributes)))
        self.__db.execute(cmd, values)
        self.__db.commit()

    def update_object(self, live_object):
        stored_object = self.get_object(type(live_object),
                                        id=live_object.id)
        if stored_object is None:
            self.save_object(live_object)
            return
        
        if live_object == stored_object:
            return

        # Comprobar cada atributo
        table, attributes = _get_table_and_attrs_(live_object.__class__)
        for attribute in attributes:
            if attribute == 'id':
                continue
            stored_value = getattr(stored_object, attribute)
            live_value = getattr(live_object, attribute)
            if live_value != stored_value:
                cmd = 'update %s set %s = ? where id = ?' % (table, attribute)
                self.__db.execute(cmd, (live_value, stored_object.id))
                self.__db.commit()
