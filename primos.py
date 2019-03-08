a = int(input("valor del numerador: "))
b=0
for i in range(1, a + 1):
    print("la division de:", a, i, "es:", a / i)
    if a%i==0:
        b+=1
if b>2:
    print("el numero no es primo")
else:
    print("el numero es primo")