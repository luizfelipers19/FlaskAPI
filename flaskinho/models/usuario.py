from sql_alchemy import banco

class UserModel(banco.Model):
    __tablename__ = 'usuarios'

    user_id = banco.Column(banco.Integer, primary_key=True)
    login = banco.Column(banco.String(40))
    senha = banco.Column(banco.String(40))

    def __init__(self, login, senha): #criando um construtor que salvará os atributos a partir do que foi recebido na requisição
        self.login = login
        self.senha = senha
    
    def json(self): #essa função irá realizar a conversão do objeto em um json
        return {
            'user_id': self.user_id,
            'login': self.login
        }

    @classmethod
    def find_user(cls, user_id):
        user = cls.query.filter_by(user_id=user_id).first() #fazendo uma consulta com classmethod, em que é retornado o primeiro registro que possua o atributo user_id igual ao argumento user_id passado
        if user: #se existir um usuário com o mesmo user_id encontrado
            return user #retorna esse usuario
        return None #caso não exista, retorna None

    def save_user(self):
        banco.session.add(self) #adiciona ao banco
        banco.session.commit() #confirma a modificação
    
    def delete_user(self):
        banco.session.delete(self) #deleta no banco esse registro
        banco.session.commit() #confirma as modificações
