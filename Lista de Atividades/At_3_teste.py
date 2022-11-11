from At_3 import Feira

fruta_0 = Feira ("Maca")
fruta_1 = Feira ("Banana")
fruta_2 = Feira ("Pera")
fruta_3 = Feira ("Abacate")

print ( "Ola temos essas 4 opções de Frutas para voce:", "\n")
print (" 1 -",fruta_0.fruta, "\n 2 -", fruta_1.fruta,"\n 3 -", fruta_2.fruta,"\n 4 -", fruta_3.fruta)


nome= input("Digite seu nome: ")

selecionar = int(input("Selecione o codigo da Fruta: "))

if selecionar >= 4 :
    print ('Opcao nao Encontrada')

if selecionar <= 0 :
    print ('Opcao nao Encontrada')
    
if selecionar == 1 :
    print (nome,"Voce selecionou " , "Maca")
if selecionar == 2 :
    print (nome,"Voce selecionou " , "Banana")
if selecionar == 3 :
    print (nome,"Voce selecionou " , "Pera")
if selecionar == 4 :
    print (nome,"Voce selecionou " , "Abacate")
