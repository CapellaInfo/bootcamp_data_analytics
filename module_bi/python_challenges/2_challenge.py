ativos = []

quantidadeAtivos = int(input())

for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

ativos.sort()

for words in ativos:
  print(words)