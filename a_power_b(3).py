def a_power_b(a,b):
    prod=1
    for i in range(0,b):
        prod=prod*a
    for x in range (1,b+1):
        if x>=1000:
            raise StopIteration("Pailas")
    return(prod)


while True:
    

    a=int(input("ingrese el valor de la base"))
    if a==0:
        
        print("numero es CERO")
        break
    b=int(input("ingrese el valor del exponente"))
    resu=a_power_b(a,b)
    print("el resultado de su potencia es: ",resu)
    if a ==0:
        break
    try:
        a=int(input("ingrese el valor de la base"))
        if a==0:
            print("numero es cero")
            break
        b=int(input("ingrese el valor del exponente"))
    except ValueError:
        print("ingreso una letra")
    except StopIteration:
        print("sobrepaso el limite")
