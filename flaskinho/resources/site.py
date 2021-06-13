from flask_restful import Resource
from models.site import SiteModel

class Sites(Resource):
    def get(self):
        return {'sites': [site.json() for site in SiteModel.query.all()]}

class Site(Resource):
    def get(self, url):
        site = SiteModel.find_site(url)
        if site:
            return site.json()
        return {'message':'Nenhum site foi encontrado usando essa URL'}, 404 #not found

    def post(self, url):
        if SiteModel.find_site(url):
            return {"message":"Esse site '{}' já existe!"}, 400 #bad request
        site = SiteModel(url) #se não encontrar nenhum site existente, instancia um novo site
        try: #tenta realizar a operação
            site.save_site() #salva o site no BD
            
        except:
            return {'message':'Ocorreu um erro interno ao criar um novo site'}, 500
        return site.json()

    def delete(self, url):
        site = SiteModel.find_site(url)
        if site:
            site.delete_site()
            return {'message':'Site deletado!'}
        return {'message': 'Site não encontrado'}, 404