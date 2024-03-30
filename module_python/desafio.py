# # Desafio: A Aventura do Explorador

# # Entrada
# quantidade_passos = int(input("Informe a quantidade de passos: "))

# # //TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
# # // Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
# # // Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.

# if quantidade_passos <= 0:
#   print("Nenhum passo dado na floresta.")
# else:
#   quantidade_passos_edit = range(1, quantidade_passos + 1)
#   for passo in quantidade_passos_edit: 
#     if passo == 1:
#       print(f'Explorador: {passo} passo')
#     else:
#       print(f'Explorador: {passo} passos')


# Lista para armazenar os itens
# itens = []

# # //TODO: Solicite os itens ao usuário


# for item in range(3):
#     inputs = input()
#     itens.append(inputs)

# # Exibe a lista de itens
# print("Lista de itens:")
# for item in itens:
#         print(f'- {item}')

capacidade_atual, aumento_percentual = map(int, input().split())

# // TODO: Calcule a nova capacidade do disco de Mithril
nova_capacidade = (capacidade_atual * (aumento_percentual/100)) + capacidade_atual

# // TODO: Imprima a nova capacidade
print(nova_capacidade)
