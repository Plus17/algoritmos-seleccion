#!usr/bin/python

import random 

def torneo(data):
	data2 = [data[0:25],data[25:50],data[50:75],data[75:100]]
	print ("Grupo 1 \n %s \n" %data2[0])
	print ("Grupo 2 \n %s \n" %data2[1])
	print ("Grupo 3 \n %s \n" %data2[2])
	print ("Grupo 4 \n %s \n" %data2[3])


	nazar = []
	#Se elige un undividuo al azar de cada grupo
	nazar.append(random.choice(data2[0]) )
	nazar.append(random.choice(data2[1]) )
	nazar.append(random.choice(data2[2]) )
	nazar.append(random.choice(data2[3]) )


	#Elegir el mejor del resultado anterior
	temp = 0
	for n in nazar:
		if n > temp:
			temp = n

	return temp
'''
	temp2 = 0
	for n in nazar:
		if n > temp2:
			temp2 = n

	temp3 = 0
	for n in nazar:
		if n > temp3:
			temp3 = n


	temp4 = 0
	for n in nazar:
		if n > temp4:
			temp4 = n

	temp5 = 0
	for n in nazar:
		if n > temp5:
			temp5 = n

	temp = 0
	for n in nazar:
		if n > temp:
			temp = n
'''
	
	





def ruleta(data):
	###
	#Rangos:
	#18-38
	#39-58
	#59-78
	#79-99
	###
	rango1 = []
	rango2 = []
	rango3 = []
	rango4 = []
	for n in data:
	 	if n>= 18 and n<=38:
	 		rango1.append(n)
	 	elif n>= 39 and n <=58:
	 		rango2.append(n)
	 	elif n>= 59 and n <=78:
	 		rango3.append(n)
	 	elif n>= 79 and n <=99:
	 		rango4.append(n)



	data2 = [rango1,rango2,rango3,rango4]
	print ("Grupo 1 (%d miembros) \n %s \n" % (len(rango1),rango1))
	print ("Grupo 2 (%d miembros) \n %s \n" % (len(rango2),rango2))
	print ("Grupo 3 (%d miembros) \n %s \n" % (len(rango3),rango3))
	print ("Grupo 4 (%d miembros) \n %s \n" % (len(rango4),rango4))

	eleccion_azar = random.choice(data) 

	return eleccion_azar


#Generar grupos de edades (por rangos)
#Seleccionar de manera aleatoria uno de los grupos
#Elegir el mejor del grupo seleccionado
#mostrar cada operacion en pantalla

def elitista(data):
	temp = 0
	for n in data:
		if n > temp:
			temp = n

	return temp

poblacion_inicial = [] 
 
 # Generar 100 numeros aleatorios entre 18 y 99 y guardarlos en una lista
for n in range(0, 100): 
    poblacion_inicial.append(random.randint(18, 99)) 

print ("Tamanio de la poblacion %s \n" % len(poblacion_inicial) )

#print (poblacion_inicial)
print ("##### Torneo: ##### \n")
print ("El elemento seleccionado por torneo es %s \n\n" % torneo(poblacion_inicial))

print ("##### Ruleta: #####  \n")
print ("El elemento elegido por ruleta es %s \n\n" % ruleta(poblacion_inicial))

print ("##### Elitista: #####  \n")
print ("El elemento elegido por elitismo es %s \n\n" % elitista(poblacion_inicial))


 
# Elegir 5 numeros al azar 
# random.sample(0, 5) 