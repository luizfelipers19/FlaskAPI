from flask_restful import Resource, reqparse
from models.usuario import UserModel



class Usuario(Resource):
    # /usuarios/{user_id}
    def get(self, user_id):
        user = UserModel.find_user(user_id) #salva na variável user o resultado da busca pelo user_id
        if user: #se existir um user com o user_id especificado
            return user.json()#retorna esse usuário em formato json
        return {'message':'Usuário não encontrado'}, 404 #caso não exista, retorna uma msg de erro

    def delete(self, user_id):
        user = UserModel.find_user(user_id) #procura um usuário pelo user_id passado e salva o resultado na variável user
        if user: #se existir um user
            user.delete_user() #deleta esse usuário
            return {'message': 'Usuário deletado'}
        return {'message':'Usuário não encontrado'} #caso o usuário não for encontrado, retorna essa msg de erro


class UserRegister(Resource):
    # /cadastro
    def post(self):
        atributos = reqparse.RequestParser() #
        atributos.add_argument('login', type=str, required=True, help="O campo 'login' não pode ser deixado em branco!")
        atributos.add_argument('senha', type=str, required=True, help="O campo 'senha' não pode ser deixado em branco!")
        dados = atributos.parse_args()

        if UserModel.find_by_login(dados['login']):
            return {"message":"The login '{}' already exists." .format(dados['login'])}

        user = UserModel(**dados)
        user.save_user()
        return {"message":"Usuário com sucesso mlk"}, 201



