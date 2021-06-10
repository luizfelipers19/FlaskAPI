from flask_restful import Resource, reqparse

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
        
        #criação de um objeto que receberá os valores passados
        novo_hotel = {
            'hotel_id':hotel_id, #o ID do hotel será passado pela URL na requisição
            'nome':dados['nome'], #salva o valor passado por parâmetro e contido na lista, com index de Nome, na variável Nome
            'estrelas':dados['estrelas'], #salva o valor passado por parâmetro e contido na lista, com index de Estrelas, na variável Estrelas
            'diaria': dados['diaria'],#salva o valor passado por parâmetro e contido na lista, com index de Diaria, na variável Diaria
            'cidade': dados['cidade']#salva o valor passado por parâmetro e contido na lista, com index de Cidade, na variável Cidade
        }

        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self,hotel_id):

        dados = Hotel.argumentos.parse_args()
        novo_hotel = {'hotel_id': hotel_id, **dados}

        hotel = Hotel.findHotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201 #created

    def delete(self, hotel_id):
        pass