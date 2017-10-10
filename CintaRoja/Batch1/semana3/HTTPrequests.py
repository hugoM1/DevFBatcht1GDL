import requests

url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=cruise&key=AIzaSyBSa0SUjt7GVytZzWuzp32_nbby0RNBoNE'
response = requests.get(url)

json_object_response = response.json()


class PlacesResponse(object):
    def __init__(self, place_object_response):
        self.__place_object_response = place_object_response
        self.html_attributions = self.__place_object_response['html_attributions']
        self.results = []

    def get_results(self):
        for place in self.__place_object_response['results']:
            self.results.append(Place(place))
        return self.results


class Place(object):
    def __init__(self, place):
        self.__place = place
        self.icon = self.__place['icon']
        self.id = self.__place['id']

places = PlacesResponse(json_object_response).get_results()
for place in places:
    print place.icon

