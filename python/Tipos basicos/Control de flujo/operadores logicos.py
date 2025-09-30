gas = True
encendico = True

if gas and encendico:
    print ("puedes avanzar")

#and solo va a imprimir en pantalla si es que las dos varibles son verdaderas
# pero de lo contrario si uno es falso no mostrara nada en pantalla, podemos usar solo if o else para que nos envie otro mensaje de error


gas = False
encendico = True

if gas and encendico:
    print ("puedes avanzar")

else:
    print ("te falta gas para avanzar")
#mensaje de error por que falta gas 
