#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""palabra = input ("Escribe una frase porfavor: ")

for i in range(1,11):
    print (f"{i}. {palabra} ")


"""


#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""edad = int (input ("Escribe tu edad actual: "))
    
for i in range(1,20):
    print (i)
    if i == edad:
        print (f"encontrado, usted tiene {edad} años de edad")
        break

else:
    print ("edad no encontrada")"""



#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas

"""numero_entero = int(input("Dame por favor un numero entero: "))

for i in range (1,100):
    if i % 2 !=0:
        print (i)
    if i == numero_entero:
        print (F"Numero {numero_entero} encontrado")
        break

numero_entero = int(input("Dame por favor un número entero: "))

impares = [str(i) for i in range(1, numero_entero + 1) if i % 2 != 0]
print(", ".join(impares)) """



#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

num_entero = int (input("Dame por favor un numero entero positivo: "))

"""for i in range (100,-1,-1):    
    print (i)
    if i == num_entero:
        print ("numero encontrado")
        break
    """
atras = [str(i) for i in range (100 ,num_entero  -1,-1) ]
print (", ".join(atras))