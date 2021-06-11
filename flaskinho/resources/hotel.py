from flask_restful import Resource, reqparse
from models.hotel import HotelModel

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

    #declarando os argumentos como um atributo da classe Hotel
    argumentos = reqparse.RequestParser()
    #recebendo os valores pela chave, que serão usados para compor o novo objeto da classe Hotel
    argumentos.add_argument('nome')  
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
    

    def findHotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None


    def get(self, hotel_id):
        hotel = Hotel.findHotel(hotel_id)
        if hotel:
            return hotel
        return {"message":"Hotel not found!"}, 404 #status code de erro

    def post(self,hotel_id):
        

        dados = Hotel.argumentos.parse_args() #cria uma lista com os argumentos passados
        #
        hotel_objeto = HotelModel(hotel_id, **dados) #criando um novo objeto da classe HotelModel que será construído a partir da nossa lista dados que recebe os argumentos passados
        novo_hotel = hotel_objeto.json() #conversão do nosso novo objeto para o formato json, e salvando em uma nova variável
        #salvando o novo objeto json na nossa lista de hoteis
        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self,hotel_id):

        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados) #criando o hotel_objeto da mesma forma do metodo POST
        novo_hotel = hotel_objeto.json()

        hotel = Hotel.findHotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201 #created

    def delete(self, hotel_id):
        global hoteis #precisando declarar uma referência a nossa variável global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id] #list compreension que filtra pelos valores que são diferentes do hotel_id passado, deixando na lista apenas os que não são o id passado, e deletando o id passado por argumento
        return {'message':'Hotel Deleted!'} #mensagem de retorno