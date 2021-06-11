from flask_restful import Resource, reqparse
from models.hotel import HotelModel

# hoteis = [
#     {
#     'hotel_id':'alpha',
#     'nome': 'Alpha Hotel',
#     'estrelas': 4.3,
#     'diaria': 420.43,
#     'cidade':'Rio de Janeiro'

#     },
#     {
#     'hotel_id':'bravo',
#     'nome': 'Bravo Hotel',
#     'estrelas': 3.3,
#     'diaria': 220.99,
#     'cidade':'Florianopolis'

#     },
#     {
#     'hotel_id':'charlie',
#     'nome': 'Charlie Hotel',
#     'estrelas': 2.9,
#     'diaria': 150.49,
#     'cidade':'Monte Verde'

#     },
# ]




class Hoteis(Resource): ##lista de hoteis
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]} #retorna um dicionário com uma lista de todos os hoteis formatados em Json, a partir do nosso HotelModel. 
        #dessa forma, todos serão buscados no banco de dados criado



class Hotel(Resource): #trabalhando com um hotel único

    #declarando os argumentos como um atributo da classe Hotel
    argumentos = reqparse.RequestParser()
    #recebendo os valores pela chave, que serão usados para compor o novo objeto da classe Hotel
    argumentos.add_argument('nome')  
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
    



    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json() #retorna um objeto, que é transformado para o formato JSON
        return {"message":"Hotel not found!"}, 404 #status code de erro

    def post(self,hotel_id):
        #Se o hotel_id passado já existir no nosso banco, retornará uma mensagem de erro, avisando que não será salvo pois já existe
        if HotelModel.find_hotel(hotel_id): #acessando o método de classe find_hotel do nosso HotelModel
            return {"message": "Hotel id '{}' already exists" .format(hotel_id)}, 400

        #se o hotel não existir, será criado um novo objeto com os atributos passados
        dados = Hotel.argumentos.parse_args() #cria uma lista com os argumentos passados
        #
        hotel = HotelModel(hotel_id, **dados) #criando um novo objeto da classe HotelModel que será construído a partir da nossa lista dados que recebe os argumentos passados
        hotel.save_hotel() #utilizando a função criada em Hotel Models para salvar o hotel criado
        return hotel.json() #retornando o hotel salvo em formato JSON


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