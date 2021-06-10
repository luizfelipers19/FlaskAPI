from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

hoteis = [
    {
    'hotel_id':'alpha',
    'nome': 'Alpha Hotel',
    'estrelas': 4.3,
    'diaria': 420.43,
    'cidade':'Rio de Janeiro'

    },
    {
    'hotel_id':'bravo',
    'nome': 'Bravo Hotel',
    'estrelas': 3.3,
    'diaria': 220.99,
    'cidade':'Florianopolis'

    },
    {
    'hotel_id':'charlie',
    'nome': 'Charlie Hotel',
    'estrelas': 2.9,
    'diaria': 150.49,
    'cidade':'Monte Verde'

    },
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}

api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
    app.run(debug=True)