#Se desea saber cuántos meses han transcurrido entre los mismos inicios de dos años cualesquiera dados.#
print ("Bienvenido, en este programa te diré cuantos meses hay entre un año y otro.")
primerAño = input ("Escribe el primer año: ") 
segundoAño = input ("Escribe el segundo y último año: ") 
if (int(primerAño) > int(segundoAño)):
   diferenciaDeAños1 = (int(primerAño)-int(segundoAño))
   resultadoFinal = (diferenciaDeAños1*12) 
   print ("La cantidad de meses entre" + " " + str(segundoAño) + " " + "y" + " " + str(primerAño) + " " + "son" + " " + str(resultadoFinal)) 

elif (int(primerAño) < int(segundoAño)):
   diferenciaDeAños2 = (int(segundoAño)-int(primerAño))
   resultadoFinal2 = (diferenciaDeAños2*12) 
   print ("La cantidad de meses entre" + " " + str(primerAño) + " " + "y" + " " + str(segundoAño) + " " + "son" + " " + str(resultadoFinal2)) 

else: 
     print ("La cantidad de meses es 0 porque usteded a seleccionado el mismo año dos veces")