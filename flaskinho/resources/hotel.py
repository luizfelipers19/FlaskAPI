from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required

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
    argumentos.add_argument('nome', type=str, required=True, help="Esse campo 'nome' não pode ser deixado em branco")   #Exigindo esses atributos nos argumentos e passando o tipo de cada um
    argumentos.add_argument('estrelas', type=float, required=True, help="O campo 'estrelas' não pode ser deixado em branco") #Exigindo esses atributos nos argumentos e passando o tipo de cada um
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
    



    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json() #retorna um objeto, que é transformado para o formato JSON
        return {"message":"Hotel not found!"}, 404 #status code de erro

    @jwt_required()
    def post(self,hotel_id):
        #Se o hotel_id passado já existir no nosso banco, retornará uma mensagem de erro, avisando que não será salvo pois já existe
        if HotelModel.find_hotel(hotel_id): #acessando o método de classe find_hotel do nosso HotelModel
            return {"message": "Hotel id '{}' already exists" .format(hotel_id)}, 400

        #se o hotel não existir, será criado um novo objeto com os atributos passados
        dados = Hotel.argumentos.parse_args() #cria uma lista com os argumentos passados
        #
        hotel = HotelModel(hotel_id, **dados) #criando um novo objeto da classe HotelModel que será construído a partir da nossa lista dados que recebe os argumentos passados
        
        try:
            hotel.save_hotel() #utilizando a função criada em Hotel Models para salvar o hotel criado
        except:
            return {'message': 'Aconteceu um erro interno tentando salvar esse registro de hotel.'}, 500 #Erro interno de servidor
        
        return hotel.json() #retornando o hotel salvo em formato JSON

    @jwt_required()
    def put(self,hotel_id):

        dados = Hotel.argumentos.parse_args()
        #hotel = HotelModel(hotel_id, **dados) #criando o hotel_objeto da mesma forma do metodo POST
      
      

        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados) #se o hotel for encontrado, é atualizado através dos key-word arguments
            hotel_encontrado.save_hotel() #salva no banco o hotel atualizado
            return hotel_encontrado.json(), 200 #retorna o código 200 de sucesso OK
        hotel = HotelModel(hotel_id, **dados) #se não encontrar um hotel pelo id passado, cria uma nova instância
        
        try:
            hotel.save_hotel()
        except:
            return {'message':'Ocorreu um erro interno em nosso servidor ao tentar salvar esse registro'},500
        return hotel.json(), 201 #created

    @jwt_required()
    def delete(self, hotel_id):
        
        #hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id] #list compreension que filtra pelos valores que são diferentes do hotel_id passado, deixando na lista apenas os que não são o id passado, e deletando o id passado por argumento
        
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {"message":"Ocorreu um erro interno na hora de deletar esse registro pelo lado do servidor"}, 500
            return {'message':'Hotel Deleted!'} #mensagem de retorno
        return {'message':'Hotel not found!'}, 404