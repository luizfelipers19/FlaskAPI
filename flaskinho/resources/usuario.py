from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST

atributos = reqparse.RequestParser() #
atributos.add_argument('login', type=str, required=True, help="O campo 'login' não pode ser deixado em branco!")
atributos.add_argument('senha', type=str, required=True, help="O campo 'senha' não pode ser deixado em branco!")

class Usuario(Resource):
    # /usuarios/{user_id}
    def get(self, user_id):
        user = UserModel.find_user(user_id) #salva na variável user o resultado da busca pelo user_id
        if user: #se existir um user com o user_id especificado
            return user.json()#retorna esse usuário em formato json
        return {'message':'Usuário não encontrado'}, 404 #caso não exista, retorna uma msg de erro

    @jwt_required()
    def delete(self, user_id):
        user = UserModel.find_user(user_id) #procura um usuário pelo user_id passado e salva o resultado na variável user
        if user: #se existir um user
            user.delete_user() #deleta esse usuário
            return {'message': 'Usuário deletado'}
        return {'message':'Usuário não encontrado'} #caso o usuário não for encontrado, retorna essa msg de erro


class UserRegister(Resource):
    # /cadastro
    def post(self):
        
        dados = atributos.parse_args()

        if UserModel.find_by_login(dados['login']):
            return {"message":"The login '{}' already exists." .format(dados['login'])}

        user = UserModel(**dados)
        user.save_user()
        return {"message":"Usuário com sucesso mlk"}, 201

class UserLogin(Resource):

    @classmethod
    def post(cls):
        dados = atributos.parse_args()

        user = UserModel.find_by_login(dados['login'])
        if user and safe_str_cmp(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {"access_token": token_de_acesso},200
        return {"message":"The username or password is incorrect."}, 401 #Unauthorized


class UserLogout(Resource): 
    #para deslogar um usuário, precisamos procurar o id do token respectivo e desativá-lo

    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti'] #JWT TOKEN IDENTIFIER
        BLACKLIST.add(jwt_id)
        return {'message':'Deslogado com sucesso'}, 200


