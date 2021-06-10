from flask_restful import Resource

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

class Hoteis(Resource): ##lista de hoteis
    def get(self):
        return {'hoteis': hoteis}



class Hotel(Resource): #trabalhando com um hotel único
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {"message":"Hotel not found!"}, 404 #status code de erro

    def post(self,hotel_id):
        pass

    def put(self,hotel_id):
        pass

    def delete(self, hotel_id):
        pass