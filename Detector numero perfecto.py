def perfecto (n):
    suma = 0
    for i in range (1, n):
        if n%i == 0:
            suma = suma + i
            
    if suma == n:
        return True
    else:
        return False
    
n = int(input("Ingrese un valor: "))

if perfecto (n) == True:
    print("Es perfecto")
    
else:
    print("No es perfecto")

            



