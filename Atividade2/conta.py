class Conta:

    def __init__(self, codigo, titular, saldo):
       
        self.__codigo = codigo
        self.__titular = titular
        self.__saldo = saldo
        

    def extrato(self):
        print("Saldo de {} {} ".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)



c1 = Conta(1, 'Fulano', 1000)
c2 = Conta(2, 'Ciclano', 400)
