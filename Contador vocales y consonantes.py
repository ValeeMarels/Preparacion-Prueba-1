#Cuantas vocales y cuantas consonantes hay en un texto#

Texto = (input("Ingrese texto: "))

contador_vocales= 0
contador_consonantes= 0
for i in (Texto):
    if i == "a" or i== "e" or i== "i" or i== "o" or i=="u":
        contador_vocales = contador_vocales + 1
        
    
    else:
        contador_consonantes = contador_consonantes + 1
        
print(contador_consonantes, "consonantes")
print(contador_vocales, "vocales")
