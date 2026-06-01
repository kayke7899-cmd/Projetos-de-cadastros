#lista para armazenar os nomes dos pilotos e dos carros
nome_do_piloto = []
nome_do_carro = []

#1. Criamos duas listas vazias
print("=== LANÇAMENTO DE CARROS ===")
while True:
    nome_do_piloto_input = input("Nome do piloto (ou 'sair' para terminar): ")
    if nome_do_piloto_input.lower() == "sair":
        break #intorrompe o loop
    nome_do_carro_input = input(f"Nome do carro de {nome_do_piloto_input}: ")

#armazenamos os dados nas listas
    nome_do_piloto.append(nome_do_piloto_input)
    nome_do_carro.append(nome_do_carro_input)
    print(" Registrado!\n")

    #mostrar o resultado final 
print('\n LISTA DE PILOTOS E CARROS:')
for i in range(len(nome_do_piloto)):
    print(f'{nome_do_piloto[i]}->{nome_do_carro[i]}')