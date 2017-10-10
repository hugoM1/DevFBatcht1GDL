# coding=utf-8
import json


class TheData(object):
    def __init__(self, data_object):
        self.data = data_object
        self.limit = data_object['limit']
        self.total = data_object['total']
        self.count = data_object['count']
        self.results = data_object['results']

    def get_results(self):
        return Results(self.results)


class Results(object):
    def __init__(self, results):
        self.results = results

    def get_personaje(self, position):
        return Personaje(self.results[position])


class Personaje(object):
    def __init__(self, personaje):
        self.__personaje = personaje
        self.__id = personaje['id']
        self.__name = personaje['name']
        self.__the_comics = []

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_thumbnail(self):
        return Thumbnail(self.__personaje['thumbnail'])

    def get_comics(self):
        return Comic(self.__personaje['comics'])


class Thumbnail(object):
    def __init__(self, thumb):
        self.extension = thumb['extension']
        self.path = thumb['path']


class Comic(object):
    def __init__(self, comic):
        self._comic = comic
        self.collectionURI = self._comic['collectionURI']

    def get_collectionURI(self):
        return self.collectionURI


json_file = open('marvel.json').read()
objeto_json = json.loads(json_file)
data = TheData(objeto_json['data'])

the_results = data.get_results()
personaje = [the_results.get_personaje(0)]


for persona in personaje:
    print persona.get_comics().get_collectionURI()
