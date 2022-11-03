from pymongo import MongoClient


class MongoPythonMethods:

    def __init__(self):
       self.banco = self.config_db()

    def config_db(self):
        self.cliente = MongoClient('mongodb://localhost:27017/')
        self.banco = self.cliente['service_bus_db']
        self.mensagens = self.banco['mensagens']

    def insert_one(self, msg):
        self.mensagens.insert_one(msg)

    def update_one(self, registro, novo_registro):
        self.mensagens.update_one(registro, novo_registro)

    def delete_one(self, registro):
        self.mensagens.delete_one(registro)

    def find_one(self, consulta):
        x = self.mensagens.find_one(consulta)
        print(x)

    def find_all(self):
        for x in self.mensagens.find():
            print(x)

    def query(self, consulta):
        dados = self.mensagens.find(consulta)
        for x in dados:
           print(x)






