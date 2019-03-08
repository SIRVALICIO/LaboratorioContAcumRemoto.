a=int(input("Valor deseado: "))
b=1
c=0
while b>-1 and b<a:
    print("la division entre los digitos: ",a,b,"es: ",a/(b))
    b+=1
    if a%b==0:
        c+=1
if c>2:
    print("El numero no es primo")
else:
    print("el numero es primo")