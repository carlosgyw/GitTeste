def verificar_primo(n):
    if n < 2:
        return False
    

    for i in range(2, n):
        if n % i == 0: 
            return False
            
    return True
def verificar_tudo(x,y ):
    if verificar_primo(x) and verificar_primo(y):
        soma = x + y
        if verificar_primo(soma):
            print (f"A soma de {x} e {y} eh um primo")
        else:
            print (f"A soma de {x} e {y} nao eh um primo")
    else:
        if not verificar_primo(x):
            print (f"O numero {x} nao eh primo")
        elif not verificar_primo(y):
            print (f"O numero {y} nao eh primo")
x = int(input())
y = int(input())
verificar_tudo(x, y)
