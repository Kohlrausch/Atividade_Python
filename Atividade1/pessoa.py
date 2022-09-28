class Pessoa:
    
    def __init__ (self, nome): 
        self.nome = nome
        print ('Nome: ', self.nome)

    def peso_pessoa (self, peso):
        self.peso = peso
        if (self.peso >= 50.0):
            print ('Acima do Peso')
        elif (self.peso <= 50.0):
            print ('Peso Normal')
        return peso;
