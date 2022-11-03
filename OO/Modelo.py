

class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes = self.__likes + 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()





star_wars = Filme("Uma nova esperança", 1900, 160)
star_wars.dar_like()
#print(star_wars)
#print(f"Nome: {star_wars.nome} - Ano: {star_wars.ano} - Duração: {star_wars.duracao} - Likes: {star_wars.likes}")
print("O nome do filme é: {}, o ano é {}, a duração é: {}, Likes: {}".format(star_wars.nome, star_wars.ano, star_wars.duracao, star_wars.likes))


class Serie:

    def __init__(self, nome, ano, temporadas):
        self.__nome = nome
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes = self.__likes + 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

dexter = Serie("Dexter", 1999, 8)
dexter.dar_like()
print("O nome da série é: {}, o ano é {}, a temporada é: {}, Likes: {}".format(dexter.nome, dexter.ano, dexter.temporadas, dexter.likes))

