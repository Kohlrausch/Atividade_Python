import conta from Conta

print ('SALDO')
c1.extrato()
c2.extrato()
print ('\n')

c1.transfere(float(input("Digite o valor da Transferencia: ")),c2)

print ('\n')
print ('TRANSFERENCIA')
c1.extrato()
c2.extrato()
