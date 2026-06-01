lista_titulos = []
lista_autores = []
print('=== CADASTRO DE LIVROS ===')
while True:
    titulo = input('Título do livro (ou "sair" para terminar): ')
    if titulo.lower() == 'sair':
        break

    autor = input(f'Autor do livro "{titulo}": ')

    lista_titulos.append(titulo)
    lista_autores.append(autor)

titulo = "BIBLIOTECA VIRTUAL"
largura = 30
print()
print('=' * largura)
print(titulo.center(largura))
print('=' * largura)

for i in range(len(lista_titulos)):
    print(f'Livro: {lista_titulos[i]:<15}|Autor: {lista_autores[i]}')