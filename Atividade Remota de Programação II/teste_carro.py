from carro import Carro

Carro=input ('Digite o carro: ')
capacidade_tanque=int(input('Digite a quantidade de Combustivel no tanque: '))
consumo=int(input('Digite o Consumo de KM por litro do carro: '))
km=int(input('Digite a distancia de KM percorrida: '))

calc=  (capacidade_tanque - ( km / consumo))

print (Carro,'Com ',capacidade_tanque,' Litros de Combustivel no tanque e','Fazendo ',consumo,' KM/L ,','Percorreu a distancia de ',km,'KM e',
'Ficou sobrando',calc ,'Litros de Combustivel no tanque')
