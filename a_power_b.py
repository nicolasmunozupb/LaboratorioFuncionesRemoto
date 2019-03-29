def a_power_b(a,b):
    prod=1
    for i in range(0,b):
        prod=prod*a
    print(prod)

a=int(input("ingrese la base"))
b=int(input("ingrese potencia"))
a_power_b(a,b)
