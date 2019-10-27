#Cuantos numeros perfectos hay en un intervalo de numeros#

def perfecto (n):
    suma = 0
    for i in range (1, n):
        if n%i == 0:
            suma = suma + i
            
    if suma == n:
        return True
    else:
        return False
    
def intervalo (n):
    contador= 0
    for c in range (1, n+1):
        if perfecto (c) == True:
            contador = contador + 1
    return contador

n = int(input("Ingrese un intervalo: "))
resultado = intervalo (n)
print(resultado)
        
