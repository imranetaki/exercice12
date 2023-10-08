x=int(input("entrer un entier x svp : "))
y=int(input("entrer un autre entier y svp : "))
if x*y>0 :
    z=x
    x=y
    y=z
else :
    z=x+y 
    w=x*y
    x=z
    y=w

print("la nouvelle valeur de x est : ",x)
print("la nouvelle valeur de y est : ",y)
