#Se requiere llenar un tanque que tiene una capacidad de 50 metros cúbicos. Haga un algoritmo que imprima las horas que tarda en llenarse dicho tanque con una manguera que tiene una capacidad de L litros de agua por minuto.#
print ("Bienvenido :D, en este programa hallaremos la cantidad necesaria de horas para llenar una pileta de 50 metros, dependiendo de la capacidad por minuto de la manguera.") 
litrosXMinuto = input ("¿Serías tan amable de comentarme cuantos litros por minuto tu manguera puede llenar? Solo escribe el número: ") 
xMinutos = (50000/int(litrosXMinuto))
xHoras = (int(xMinutos)/60) 
horasRedondeado = round(xHoras) 
print ("Teniendo en cuenta que tu manguera tiene la capacidad de" + " " + str(litrosXMinuto) + " " + "tu pileta tardará" + " " + str(xMinutos) + " " + "minutos en llenarse, que son" + " " + str(horasRedondeado) + " " + "horas. (aproximado)") 


