# Aula 16 - 29/11/2019
# ?????????

from faixa import criar_faixa, salvar_faixa, ler_faixa


# Cadastro de playlist
# Lendo musica, artista e album

musica = input('Digite uma música: ')
artista = input('Digite um artista: ')
album = input('Digite o nome do albúm: ')

faixa1 = criar_faixa(musica, artista, album)
salvar_faixa(faixa1)
lista = ler_faixa()

for faixa in lista:
    print(f"{faixa['musica']} - {faixa['artista']} - {faixa['album']}")