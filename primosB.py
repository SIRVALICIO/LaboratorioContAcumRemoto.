a=int(input("Valor deseado: "))
b=1
c=0
while  b<a+1:


    if a%b==0:
        c+=1

    b+=1

if c>2:
    print("El numero no es primo")
else:
    print("el numero es primo")