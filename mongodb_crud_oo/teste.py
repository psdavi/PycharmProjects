
from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017/')

#-------------------------------------------- CREATE DATABASE
banco = cliente['service_bus_db']

#-------------------------------------------- CREATE COLLECTION
mensagens = banco['mensagens']

#--------------------------------------------FIND ONE
x = banco.mensagens.find_one()
print(x)

#--------------------------------------------FIND ALL
for x in banco.mensagens.find():
    print(x)


#-------------------------------------------- QUERY
consulta = {"Titulo": ""}
dados = mensagens.find(consulta)
for x in dados:
    print(x)

#--------------------------------------------INSERT ONE
banco.mensagens.insert_one({'titulo': "Conteúdo da Mensagem para TiTi"})


#-----------------------------------------------UPDATE ONE
registro = {"titulo": "Conteúdo da Mensagem para Otiliano"}
novo_registro = {"$set": {"titulo": "Conteúdo da Mensagem para Davi"}}
banco.mensagens.update_one(registro, novo_registro)


#-----------------------------------------------DELETE ONE
registro = {"titulo": "Conteúdo da Mensagem para Davi"}
banco.mensagens.delete_one(registro)


#-----------------------------------------------DROP COLLECTION
banco.mensagens.drop()



