from sql_alchemy import banco

#criando o Model para o SITE


class SiteModel(banco.Model):
    __tablename__ = 'sites' #criará uma tabela Sites
    site_id = banco.Column(banco.Integer, primary_key=True)
    url = banco.Column(banco.String(80))
    hoteis = banco.relationship('HotelModel') #Retornará uma lista de hoteis pois estamos declarando o relacionamento entre a tabela de Hoteis e Sites.
    

    def __init__(self, url):
        self.url = url
    
    def json(self):
        return {
            'site_id':self.site_id,
            'url': self.url,
            #cada site terá uma lista de hoteis
            'hoteis':[hotel.json() for hotel in self.hoteis] #usando list comprehension para retornar uma lista de hoteis que estão relacionados ao nosso site
        }

    @classmethod
    def find_site(cls, url):
        site = cls.query.filter_by(url = url).first() #SELECT * FROM hoteis WHERE hotel_id = hotel_id (procura na tabela hoteis todos os registros que o hotel_id é igual ao hotel_id que estamos passando)
        if site:
            return site
        return None
    
    def save_site(self):
        banco.session.add(self) #usando o session.add() do sqlalchemy para adicionar o registro no banco
        banco.session.commit() #salvando o registro adicionado

    

    def delete_site(self):
        banco.session.delete(self) #usa a função delete da session do SQLAlchemy
        banco.session.commit()