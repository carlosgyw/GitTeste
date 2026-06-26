def remover_repetidos(texto):
  if len(texto) <= 1:
        return texto
  primeira_letra = texto[0]
  segunda_letra = texto[1]
  resto_do_texto = texto[1:]
  if primeira_letra == segunda_letra:
        return remover_repetidos(resto_do_texto)
  else:
        return primeira_letra + remover_repetidos(resto_do_texto)

while True:
  linha = input()
  if linha == '*':
        break
    
print(remover_repetidos(linha))