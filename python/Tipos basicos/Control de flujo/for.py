#El range es seguir por su cuenta la numeracion de 5, va a empezar de 0,1,2,3 y 4
#La variable numero es donde nosotros vamos tomar para que nos muestre en pantalla ya que esa variable esta de la mano con el range(5)


buscar = 10
for numero in range(5):
    print (numero)
    if numero == buscar:
        print ("encontrado",buscar) 
        break
 

else:
    print ("numero no encontrado")



