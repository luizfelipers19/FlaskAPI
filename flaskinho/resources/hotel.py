from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required
import sqlite3



def normalize_path_params(cidade=None,
                            estrelas_min=0,
                            estrelas_max=5,
                            diaria_min=0,
                            diaria_max=100000,
                            limit = 50,
                            offset = 0, **dados):
    if cidade:
        return {
            'estrelas_min': estrelas_min,
            'estrelas_max': estrelas_max,
            'diaria_min': diaria_min,
            'diaria_max': diaria_max,
            'cidade': cidade,
            'limit':limit,
            'offset':offset
        }
    return {
        'estrelas_min': estrelas_min,
        'estrelas_max': estrelas_max,
        'diaria_min': diaria_min,
        'diaria_max': diaria_max,
        'limit':limit,
        'offset':offset
    }


#path /hoteis?cidade=Rio de Janeiro  <= filtragem de hoteis por cidade

#implementando a filtragem de hoteis e paginação
path_params = reqparse.RequestParser()
path_params.add_argument('cidade', type=str)
path_params.add_argument('estrelas_min', type=float)
path_params.add_argument('estrelas_max', type=float)
path_params.add_argument('diaria_min', type=float)
path_params.add_argument('diaria_max', type=float)
path_params.add_argument('limit', type=float)
path_params.add_argument('offset', type=float)

class Hoteis(Resource): ##lista de hoteis
    def get(self):  #realizar paginação e filtração
        
        connection = sqlite3.connect('banco.db') #criando uma nova conexão ao nosso banco existente
        cursor = connection.cursor()#criação do cursor

        dados = path_params.parse_args()
        dados_validos = {chave: dados[chave] for chave in dados if dados['chave'] is not None} #usa dictionary comprehension para filtrar os dados (declarados acima) onde o valor de cada item (chave) não for nulo
        parametros = normalize_path_params(**dados_validos)
        
        if parametros.get('cidade'): #consultando se existe o valor salvo no campo Cidade
            consulta = "SELECT * FROM hoteis \
            WHERE (estrelas > ? and estrelas < ? \
                 and diaria > ? and diaria < ? ) \
                     LIMIT ? OFFSET ?"

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