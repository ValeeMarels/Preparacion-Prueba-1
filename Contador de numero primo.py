def primo (n):
    contador = 0
    for i in range (1, n+1):
        if n%i == 0:
            contador = contador + 1
            
    if contador == 2:
        return True
    else:
        return False
    

def intervalo(n):
    contador = 0
    for c in range (1, n+1):
        if primo(c) == True:
            contador = contador + 1
    return contador

n = int(input("Ingrese valor del intervalo: "))
resultado = intervalo(n)
print(resultado)
    
    