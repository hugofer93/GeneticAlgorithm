from numpy.random import random

def genPairs(poblacion):
	vect = []
	aux = []
	
	for i in range(poblacion):
		vect.append(i)
		aux.append(-1)
	
	ite = 0

	while aux.count(-1) >= 1:
		posicion = int((len(vect) - 0) * random() + 0)
		if ite == 0:
			while posicion == 0:
				posicion = int((len(vect) - 0) * random() + 0)
		
		while posicion == ite or vect[posicion] == -1:
			posicion = int((len(vect) - 0) * random() + 0)

		if aux[ite] == -1:
			aux[ite] = vect[posicion]
			aux[posicion] = vect[ite]
			vect[posicion] = -1
			vect[ite] = -1

		ite = ite + 1

	return aux