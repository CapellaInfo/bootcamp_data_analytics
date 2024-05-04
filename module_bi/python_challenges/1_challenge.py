valor = float(input())

saldo_atual = 0

if valor > 0:
  saldo_atual += valor
  print("Deposito realizado com sucesso! \n Saldo atual: R$ {:.2f}".format(saldo_atual))
elif valor < 0:
  print("Valor invalido! Digite um valor maior que zero.")
else:
  print("Encerrando o programa...")