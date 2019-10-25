a = int(input("Valor para a: "))
b = int(input("Valor para b: "))
c = int(input("Valor para c: "))

if a>b>c:
    print( a, b, c )
    
elif b>a>c:
    print( b, a, c )

elif b>c>a:
    print( b, c, a )

elif c>b>a:
    print( c, b, a)
    
elif c>a>b:
    print( c, a, b )
    
elif a>c>b:
    print( a, c, b )