from ast import Break
from At_5 import Cadastro

print ('    +++ MENU +++')
print (' 1- Cadastrar Alunos','\n','2- Cadastrar Professores','\n','3- Cadastrar Cursos','\n','4- Sair','\n')
op=int(input('Digite a Opcao:'))

if op == 1:
    print ('Cadastro Alunos','\n')
    al_nome= input ('Digite o Nome:')
    al_endereco= input ('Digite o Endereco:')
    al_telefone= int (input ('Digite o Telefone:'))

if op == 2:
    print ('Cadastro Professores','\n')
    pro_nome= input ('Digite o Nome:')
    pro_endereco= input ('Digite o Endereco:')
    pro_telefone= int (input ('Digite o Telefone:'))

if op == 3:
    print ('Cadastro Cursos','\n')
    cursos=input ('Digite o Nome do Curso:')

if op == 4:
    print ('Opcao Sair')
    Break
