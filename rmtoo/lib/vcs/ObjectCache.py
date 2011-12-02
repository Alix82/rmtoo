'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Caches objects.
   This class caches objects.  The ID is the unique VCS id.
   
 (c) 2010-2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

from types import ListType
from rmtoo.lib.logging.EventLogging import tracer
from rmtoo.lib.RMTException import RMTException

class ObjectCache:
    '''Stores objects from different types under a unique id.
       Each class has a separate store: it is possible to 
       have the same id for multiple objects of different types.'''

    def __init__(self):
        '''Creates a cache for the given object_type.'''
        self.__objects = {}

    @staticmethod
    def __create_hashable(oid):
        '''If the oid is a list, the oid is converted into a string.'''
        tracer.debug("called: oid [%s]" % oid)
        if type(oid) == ListType:
            if len(oid) == 1:
                return oid[0]
            return '-'.join(oid)
        return oid

    def get(self, object_type, oid):
        '''Tries to receive an object with the given id.
           If found, the object is returned, if not found
           None is returned.'''
        tracer.debug("called: oid [%s]" % oid)
        loid = self.__create_hashable(oid)
        
        if self.__objects.has_key(object_type) \
            and self.__objects[object_type].has_key(loid):
            return self.__objects[object_type][loid]
        return None

    def add(self, oid, obj):
        '''Adds the given object to the cache using the given object id.
           Checks of the object is of the correct type and if
           the object is already in the cache.'''
        tracer.debug("adding object with oid [%s]" % oid)
        
        object_type = type(object)
        if not self.__objects.has_key(object_type):
            self.__objects[object_type] = {} 
        
        if oid in self.__objects[object_type]:
            raise RMTException(106, "object with oid [%s] already in cache."
                               % oid)
        self.__objects[object_type][oid] = obj