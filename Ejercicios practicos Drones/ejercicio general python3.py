#Un amigo suyo acaba de iniciar un negocio de venta de zapatos. Por ahora sólo vende tres tipos de zapatos: sandalias, tenis y mocasines. Cada tipo de zapato lo adquiere a un costo distinto y para venderlos, supone una ganancia del 55%. Cuando un cliente llega debe comprar de los tres tipos de zapatos y la cantidad que desee de cada uno de ellos. El cliente tiene derecho a un 8% de descuento sobre la compra que realiza. Ayúdele a su amigo a crear un programa que, para un cliente dado, muestre su nombre, el valor de la venta sin descuento, el descuento, valor de la venta con descuento y valor de la venta incluyendo IVA (venta neta final).#
print ("Bienvenido a este programa, el cual ayudará en el control de ventas") 
nombreCliente = input ("Ingrese el nombre del comprador: ") 
cantidadS = input ("Ingrese la cantidad de pares de Sandalias a vender: ")
cantidadT = input ("Ingrese la cantidad de pares de Tenis a vender: ") 
cantidadM = input ("Ingrese la cantidad de pares de Mocasines a vender: ")
if (int(cantidadS) > 0 ):
    precioS = input ("Ingrese el precio original del producto (sin ganancias y/o impuestos): $")
else: precioS = 0
if (int(cantidadT) > 0):
   precioT = input ("Ingrese el precio original del producto (sin ganancias y/o impuestos): $")
else: precioT = 0
if (int(cantidadM) > 0):
   precioM = input ("Ingrese el precio original del producto (sin ganancias y/o impuestos): $")
else: precioM = 0 
precioSCc = (int(precioS)/100*55)
precioSg = (int(precioS) + precioSCc)
precioTCc = (int(precioT)/100*55)
precioTg = (int(precioT) + precioTCc)
precioMCc = (int(precioM)/100*55)
precioMg = (int(precioM) + precioMCc) 
precioSgIVA = (precioSg/100*21) 
precioSgIVAf = (precioSg + precioSgIVA)
precioTgIVA = (precioTg/100*21) 
precioTgIVAf = (precioTg + precioTgIVA) 
precioMgIVA = (precioMg/100*21) 
precioMgIVAf = (precioTg + precioTgIVA) 
sumaPcGeI = (precioSgIVAf + precioTgIVAf + precioMgIVAf) 
preferenciaCliente = input ("¿Desea el cliente un descuento del 8%?: ") 
if (preferenciaCliente == "Si"):
   desc8 = (sumaPcGeI/100*8)
   precioFinalDesc = (sumaPcGeI-desc8) 
   print ("El descuento se ha aplicado con éxito (total= " + str(precioFinalDesc) +")")
   print ("Se han procesado todos los datos correspondientes: ") 
   print ("Nombre del comprador: " + nombreCliente)
   print ("Valor de la venta: " + str(sumaPcGeI))
   print ("Valor de la venta con descuento del 8%: " + str(precioFinalDesc))
   print ("Precio total de la compra a pagar: " + str(precioFinalDesc))
elif (preferenciaCliente == "si"): 
     desc8 = (sumaPcGeI/100*8)
     precioFinalDesc = (sumaPcGeI-desc8) 
     print ("El descuento se ha aplicado con éxito (total= " + str(precioFinalDesc) +")")
     print ("Se han procesado todos los datos correspondientes: ") 
     print ("Nombre del comprador: " + nombreCliente)
     print ("Valor de la venta: " + str(sumaPcGeI))
     print ("Valor de la venta con descuento del 8%: " + str(precioFinalDesc))
     print ("Precio total de la compra a pagar: " + str(precioFinalDesc))
elif (preferenciaCliente == "Sí"): 
     desc8 = (sumaPcGeI/100*8) 
     precioFinalDesc = (sumaPcGeI-desc8) 
     print ("El descuento se ha aplicado con éxito (total= " + str(precioFinalDesc) +")")
     print ("Se han procesado todos los datos correspondientes: ") 
     print ("Nombre del comprador: " + nombreCliente)
     print ("Valor de la venta: " + str(sumaPcGeI))
     print ("Valor de la venta con descuento del 8%: " + str(precioFinalDesc))
     print ("Precio total de la compra a pagar: " + str(precioFinalDesc))
elif (preferenciaCliente == "sí"):
     desc8 = (sumaPcGeI/100*8) 
     precioFinalDesc = (sumaPcGeI-desc8)
     print ("El descuento se ha aplicado con éxito (total= " + str(precioFinalDesc) +")")
     print ("Se han procesado todos los datos correspondientes: ") 
     print ("Nombre del comprador: " + nombreCliente)
     print ("Valor de la venta: " + str(sumaPcGeI))
     print ("Valor de la venta con descuento del 8%: " + str(precioFinalDesc))
     print ("Precio total de la compra a pagar: " + str(precioFinalDesc))
else: 
    precioFinalDesc= sumaPcGeI
    print ("No se ha aplicado el descuento.")
print ("Se han procesado todos los datos correspondientes: ") 
print ("Nombre del comprador: " + nombreCliente)
print ("Valor de la venta: " + str(sumaPcGeI))
print ("Valor de la venta con descuento del 8%: " + " " + "*No se ha registrado ningún descuento*")
print ("Precio total de la compra a pagar: " + str(sumaPcGeI)) 

