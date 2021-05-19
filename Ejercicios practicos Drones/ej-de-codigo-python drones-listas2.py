usuarios = ["marta" , "jose" , "pepe" , "juana" , "luisa" , "marcos"] 
print (usuarios[2]) 
#listas#
usuarios[2] = "Emanuel" 
print (usuarios[2]) 

print (usuarios[1:4]) #propiedad de listas# 

print ("Lista original: ", usuarios) #no se puede poner un +, tiene que estar separado, como si fueran dos print#

print ("Ramon" in usuarios) 
print ("marta" in usuarios) #para buscar si está o no en la lista#

print ("Ramon" not in usuarios) #lo mismo pero preguntando si es que NO está#

compras = ["naranjas", "peras", "manzanas", ["marta", [10,20], "marcos", "tomate" ]]

print (compras[3][0]) 