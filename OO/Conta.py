
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        #self.__codigo_banco = "001"

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if(self.permite_sacar(valor)):
            self.__saldo = self.__saldo - valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def __permite_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    @property
    def get_saldo(self):
        return self.__saldo

    @property
    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

#metodo statico pertence a classe, pode ser chamado sem ser passado como atributo
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {
            "BB": "001",
            "Caixa": "104",
            "Bradesco": "237"
        }

