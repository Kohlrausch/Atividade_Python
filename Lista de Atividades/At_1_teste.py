from At_1 import Viagem

viagem_0 = Viagem ("Viagem para Ceara")
viagem_1 = Viagem ("Viagem para Minas Gerais ")
viagem_2 = Viagem ("Viagem para o Rio de Janeiro")
viagem_3 = Viagem ("Viagem para o Porto Alegre")



cliente= input("Digite seu nome: ")
print (cliente, "Ola ofertamos 4 opções de viagens para voce: ")
print ("\n 1 -", viagem_0.viagem, "\n 2 -", viagem_1.viagem,"\n 3 -", viagem_2.viagem,"\n 4 -", viagem_3.viagem)

selecionar = int(input("Selecione o codigo  da viagem: "))

if selecionar >= 5 :
    print ('Opcao nao Encontrada')

if selecionar <= 0 :
    print ('Opcao nao Encontrada')
    
if selecionar == 1 :
    print (cliente,"Voce selecionou " , "Viagem para Ceara", "\n","Boa Viagem")
if selecionar == 2 :
    print (cliente,"Voce selecionou " , "Viagem para Minas Gerais", "\n","Boa Viagem")
if selecionar == 3 :
    print (cliente,"Voce selecionou " , "Viagem para Rio de janeiro", "\n","Boa Viagem")
if selecionar == 4 :
    print (cliente,"Voce selecionou " , "Viagem para Porto Alegre", "\n","Boa Viagem")
