from flask import Flask
from flask_restful import Api, Resource, abort, reqparse, marshal
from flask_apispec.views import MethodResource
import json
import socket

app = Flask(__name__)
api = Api(app)

films = json.load(open('Src/Film.json'))

# Function to display hostname and IP address
def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :  ",host_name)
        print("IP : ",host_ip)
        return host_name, host_ip
    except:
        print("Unable to get Hostname and IP")

class Health(Resource, MethodResource):
    def __init__(self) -> None:
        super().__init__()
    
    def get(self):
        return True

class Base(Resource, MethodResource):
    def __init__(self) -> None:
        super().__init__()
    
    def get(self):
        host, ip = get_Host_name_IP()
        return f'Up and runnning !!! in => {host} at address => {ip} try /films or /film/<string:title>'

class Film(Resource, MethodResource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('Title',type=str, location='json')
        self.parser.add_argument('Year',type=str, location='json')
        self.parser.add_argument('Rated',type=str, location='json')
        self.parser.add_argument('Released',type=str, location='json')
        self.parser.add_argument('Runtime',type=str, location='json')
        self.parser.add_argument('Genre',type=str, location='json')
        self.parser.add_argument('Director',type=str, location='json')
        self.parser.add_argument('Writer',type=str, location='json')
        self.parser.add_argument('Actors',type=str, location='json')
        self.parser.add_argument('Plot',type=str, location='json')
        self.parser.add_argument('Country',type=str, location='json')
        self.parser.add_argument('Awards',type=str, location='json')
        self.parser.add_argument('Poster',type=str, location='json')
        self.parser.add_argument('Metascore',type=str, location='json')
        self.parser.add_argument('imdbRating',type=str, location='json')
        self.parser.add_argument('imdbVotes',type=str, location='json')
        self.parser.add_argument('imdbID',type=str, location='json')
        self.parser.add_argument('Type',type=str, location='json')
        self.parser.add_argument('Response',type=str, location='json')
        self.parser.add_argument('Images',type=str, location='json')
        self.parser.add_argument('Response',type=str, location='json')
        super(Film,self).__init__()

    def get(self, title):
        film = [film for film in films if film['Title'] == title]
        if len(film)==0:
            abort(404)
        return film
    
    def put(self, title):
        film = [film for film in films if film['Title'] == title]
        if len(film)==0:
            abort(404)
        return film

class Films(Resource, MethodResource):
    def __init__(self) -> None:
        super().__init__()

    def get(self):
        titles = [film["Title"] for film in films]
        return titles    

api.add_resource(Base,"/")
api.add_resource(Health,"/IsHealthy")
api.add_resource(Film,"/film/<string:title>")
api.add_resource(Films,"/films")

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True) 