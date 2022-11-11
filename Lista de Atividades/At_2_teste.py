from At_2 import Biblioteca

livro_1 = Biblioteca ("Ao Farol (1927)")
livro_2 = Biblioteca("O Rei Lear (1606)")
livro_3 = Biblioteca ("Moby Dick (1851)")
livro_4 = Biblioteca ("A Divina Comédia (1304—1321)")
livro_5 = Biblioteca ("Madame Bovary (1856)")
livro_6 = Biblioteca ("Viagem ao Fim da Noite (1932)")
livro_7 = Biblioteca ("Ilíada (séc. VIII a.C.)")
livro_8 = Biblioteca ("O Livro do Desassossego (1982)")
livro_9 = Biblioteca("Pantagruel (1532)")
livro_10 = Biblioteca ("Guerra e Paz (1869)")

print ( "Ola temos essas 10 opções de livros para voce:", "\n")
print (" 1 -",livro_1.livro, "\n 2 -", livro_2.livro,"\n 3 -", livro_3.livro,"\n 4 -", livro_4.livro,
"\n 5 -", livro_5.livro,"\n 6 -", livro_6.livro,"\n 7 -", livro_7.livro,"\n 8 -", livro_8.livro,
"\n 9 -", livro_9.livro,"\n 10 -", livro_10.livro,"\n")

nome= input("Digite seu nome: ")

selecionar = int(input("Selecione o codigo do Livro: "))

if selecionar >= 10 :
    print ('Opcao nao Encontrada')

if selecionar <= 0 :
    print ('Opcao nao Encontrada')
    
if selecionar == 1 :
    print (nome,"Voce selecionou " , "Ao Farol (1927)","\n","Boa Leitura")
if selecionar == 2 :
    print (nome,"Voce selecionou " , "O Rei Lear (1606)","\n","Boa Leitura")
if selecionar == 3 :
    print (nome,"Voce selecionou " , "Moby Dick (1851)","\n","Boa Leitura")
if selecionar == 4 :
    print (nome,"Voce selecionou " , "A Divina Comédia (1304—1321)","\n","Boa Leitura")
if selecionar == 5 :
    print (nome,"Voce selecionou " , "Madame Bovary (1856)","\n","Boa Leitura")
if selecionar == 6 :
    print (nome,"Voce selecionou " , "Viagem ao Fim da Noite (1932)","\n","Boa Leitura")
if selecionar == 7 :
    print (nome,"Voce selecionou " , "Ilíada (séc. VIII a.C.","\n","Boa Leitura")
if selecionar == 8 :
    print (nome,"Voce selecionou " , "O Livro do Desassossego (1982)","\n","Boa Leitura")
if selecionar == 9 :
    print (nome,"Voce selecionou " , "Pantagruel (1532)","\n","Boa Leitura")
if selecionar == 10 :
    print (nome,"Voce selecionou " , "Guerra e Paz (1869)","\n","Boa Leitura")
