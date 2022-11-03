from mongo import MongoPythonMethods


if __name__ == '__main__':
    MongoPythonMethods = MongoPythonMethods()
    MongoPythonMethods.insert_one({'titulo': "Conteúdo da Mensagem para Mamãe"})

    registro = {"titulo": "Conteúdo da Mensagem para TiTi"}
    novo_registro = {"$set": {"titulo": "Conteúdo da Mensagem para Micael"}}
    MongoPythonMethods.update_one(registro, novo_registro)

    registro = {"titulo": "Conteúdo da Mensagem para Davi"}
    MongoPythonMethods.delete_one(registro)

    MongoPythonMethods.find_one({'titulo': "Conteúdo da Mensagem para Davi"})

    MongoPythonMethods.find_all()

    consulta = {"Titulo": "Conteúdo"}
    MongoPythonMethods.query(consulta)


