from flask import jsonify
from json import loads
from flask import request

DB = [{"id": 0, "user": 0, "name": "City of love", "desc": "My trip to Paris", "start": 0, "end": 0, "duration": 4, "image": "paris"},
                             {"id": 1, "user": 0, "name": "New York", "desc": "My trip to NY", "start": 1663372800, "end": 1664236800, "duration": 10, "image": "ny"},
                             {"id": 2, "user": 0, "name": "Barcelona", "desc": "My trip to Barcelona", "start": 0, "end": 0, "duration": 4, "image": "barcelona"},
                             {"id": 3, "user": 0, "name": "Vienna", "desc": "My trip to Vienna", "start": 0, "end": 0, "duration": 4, "image": "vienna"},
                             {"id": 4, "user": 1, "name": "Madrid", "desc": "My trip to Madrid", "start": 0, "end": 0, "duration": 4, "image": "madrid"},
                             {"id": 5, "user": 1, "name": "Prague", "desc": "My trip to Prague", "start": 0, "end": 0, "duration": 4, "image": "prague"},
                             {"id": 6, "user": 1, "name": "Krakow", "desc": "My trip to Krakow", "start": 0, "end": 0, "duration": 4, "image": "krakow"},
                             {"id": 7, "user": 1, "name": "Sweden", "desc": "My trip to Sweden", "start": 0, "end": 0, "duration": 4, "image": "sweeden"},
                             {"id": 8, "user": 1, "name": "Moscow", "desc": "My trip to Moscow", "start": 0, "end": 0, "duration": 4, "image": "moscow"},
                             {"id": 9, "user": 1, "name": "Egypt", "desc": "My trip to Egypt", "start": 0, "end": 0, "duration": 4, "image": "egypt"},
                             {"id": 10, "user": 1, "name": "Rome", "desc": "My trip to Rome", "start": 0, "end": 0, "duration": 4, "image": "rome"},
                             {"id": 11, "user": 1, "name": "India", "desc": "My trip to India", "start": 0, "end": 0, "duration": 4, "image": "india"},
                             {"id": 12, "user": 1, "name": "Peru", "desc": "My trip to Peru", "start": 0, "end": 0, "duration": 4, "image": "peru"},
                             {"id": 13, "user": 1, "name": "China", "desc": "My trip to China", "start": 0, "end": 0, "duration": 4, "image": "china"},
                             {"id": 14, "user": 1, "name": "Malaysia", "desc": "My trip to Malaysia", "start": 0, "end": 0, "duration": 4, "image": "malaysia"}
                             ]

TRIPS = {"0": {"start": 0, "name": "City of love", "end": 0, "duration": 4, "desc": "If you have a European Union identification of some sort and you are between 18-26 years old, most museums in Paris are free", "image": "paris", "actions": {"days": [[{"name": "Notre Dame", "desc":"The line goes fast", "image": "notre", "type": "attraction"}, {"name": "Notre Dame", "desc":"The line goes fast", "image": "notre", "type": "walk", "duration": "15 minutes"}, {"name": "Eiffel Tower", "desc": "Make sure you go on the hour for the 5 min light show", "image": "tower", "type": "attraction"}],
                                                                                                                                                                                                                                                  [{"name": "Rodin Museum", "desc":"18th-century mansion & sculpture garden displaying Rodin's influential works, such as The Thinker.", "image": "rodin", "type": "attraction"}, {"type": "bus", "duration": "15 minutes"}, {"name": "Luxembourg Gardens", "desc": "The Luxembourg Gardens are one of the biggest public gardens in Paris, covering over 23 hectares. ", "image": "lux", "type": "attraction"}], []]}},                                                                                                                                 
        "1": {"start": 0, "name": "New York", "end": 0, "duration": 4, "desc": "My trip to NY", "image": "ny", "actions": {"days": [ [{"name":"Line1", "desc":"Description1","image":"rome","type":"attraction"}, {"name":"Line2", "desc":"Desc2", "image":"rome", "type":"attraction"}], [{"name":"Line1", "desc":"Desc1", "image":"vienna", "type":"attraction"}] ]}},
        "2": {"start": 0, "name": "Barcelona", "end": 0, "duration": 4, "desc": "My trip to Barcelona", "image": "barcelona", "actions": {"days": [[]]}},
        "3": {"start": 0, "name": "Vienna", "end": 0, "duration": 4, "desc": "My trip to Vienna", "image": "vienna", "actions": {"days": [[]]}},
        "4": {"start": 0, "name": "Madrid", "end": 0, "duration": 4, "desc": "My trip to Madrid", "image": "madrid", "actions": {"days": [[]]}},
        "5": {"start": 0, "name": "Prague", "end": 0, "duration": 4, "desc": "My trip to Prague", "image": "prague", "actions": {"days": [[]]}},
        "6": {"start": 0, "name": "Krakow", "end": 0, "duration": 4, "desc": "My trip to Krakow", "image": "krakow", "actions": {"days": [[]]}},
        "7": {"start": 0, "name": "Sweden", "end": 0, "duration": 4, "desc": "My trip to Sweden", "image": "sweeden", "actions": {"days": [[]]}},
        "8": {"start": 0, "name": "Moscow", "end": 0, "duration": 4, "desc": "My trip to Moscow", "image": "moscow", "actions": {"days": [[]]}},
        "9": {"start": 0, "name": "Egypt", "end": 0, "duration": 4, "desc": "My trip to Egypt", "image": "egypt", "actions": {"days": [[]]}},
        "10": {"start": 0, "name": "Rome", "end": 0, "duration": 4, "desc": "My trip to Rome", "image": "rome", "actions": {"days": [[]]}},
        "11": {"start": 0, "name": "India", "end": 0, "duration": 4, "desc": "My trip to India", "image": "india", "actions": {"days": [[]]}},
        "12": {"start": 0, "name": "Peru", "end": 0, "duration": 4, "desc": "My trip to Peru", "image": "peru", "actions": {"days": [[]]}},
        "13": {"start": 0, "name": "China", "end": 0, "duration": 4, "desc": "My trip to China", "image": "china", "actions": {"days": [[]]}},
        "14": {"start": 0, "name": "Malaysia", "end": 0, "duration": 4, "desc": "My trip to Malaysia", "image": "malaysia", "actions": {"days": [[]]}},
        "-1": {"start": 0, "name": "Removed", "end": 0, "duration": 4, "desc": "removed data", "image": "none", "actions": {"days": [[]]}},
        "-2": {"start": 0, "name": "Removed_ALL", "end": 0, "duration": 4, "desc": "removed data (reset)", "image": "none", "actions": {"days": [[]]}}
        }


class Users: 
    def __init__(self):
        self.__db = [{"id": 0, "name": "user", "password": "pass"}]

    def login(self, name: str, password: str):
        for user in self.__db:
            if user["name"] == name and user["password"] == password:
                return user["id"]

        return -1


class Trips:
    def __init__(self):
        self.__db = DB

        self.__trips = TRIPS

    def get_trips(self, user_id: int):
        user_id = int(user_id)
        trips = []
        for trip in self.__db:
            if trip["user"] == user_id:
                trips.append(trip)

        response = jsonify(trips)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    def get_all_trips(self):
        recommended = []
        for x in self.__db:
            if (("user", 1) in x.items()):
                recommended.append(x)
        response = jsonify(recommended)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    def get_trip(self, trip_id: int):
        self.__trips["-1"]["actions"]["days"] = self.__trips[str(trip_id)]["actions"]["days"]
        self.__trips["-2"]["actions"]["days"] = self.__trips[str(trip_id)]["actions"]["days"]
        response = jsonify(self.__trips[str(trip_id)])
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response

    def update_trip(self, trip_id: int, day: int):
        data = loads(request.data)
        self.__trips["-1"]["actions"]["days"] = self.__trips[str(trip_id)]["actions"]["days"]
        self.__trips[str(trip_id)]["actions"]["days"] = data

        response = jsonify({"message": "OK"})
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response

    def restore_trip(self, trip_id: int):
        self.__trips[str(trip_id)]["actions"]["days"] = self.__trips["-1"]["actions"]["days"]
        response = jsonify({"message": "OK"})
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response

    def reset_trip(self, trip_id: int):
        self.__trips[str(trip_id)]["actions"]["days"] = self.__trips["-2"]["actions"]["days"]
        response = jsonify({"message": "OK"})
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response

    def add_trip(self, cityname: str, imageid: str, triplen: str):
        days = []
        for i in range(0, int(triplen)):
            days.append([])
        trips_cnt = len(self.__db)
        self.__db.append({"id": trips_cnt, "user": 0, "name": cityname, "desc": "My trip to "+cityname, "start": 0, "end": 0, "duration": 4, "image": imageid})
        self.__trips[str(trips_cnt)] = {"start": 0, "name": cityname, "end": 0, "duration": 4, "desc": "My trip to "+cityname, "image": imageid, "actions": {"days": days}}

        response = jsonify({"message": "OK"})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    def delete_trip(self, tripid: str):
        i = 0
        for x in self.__db:
            if (("id", int(tripid)) in x.items()):
                self.__db.pop(i)
                break
            i = i+1
        
        del self.__trips[tripid]

        response = jsonify({"message": "OK"})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
