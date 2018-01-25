from randomBin import randomBin
from printDict import printDict
from genSelectionTable import genSelectionTable
from genCrossingTable import genCrossingTable
from genPopulationTable import genPopulationTable
from getMean import getMean

### INGRESO DE DATOS ###
print("### ALGORITMO GENETICO ###")
tamIndividuo = int(input("Ingrese Dimension de Individuo:"))
while tamIndividuo <= 0 or tamIndividuo >= 9:
	tamIndividuo = int(input("Rango aceptado [1 , 8]:"))

poblacion = int(input("Ingrese Cantidad de la Poblacion:"))
while poblacion % 2 != 0 or (poblacion <= 1 or poblacion >= 13):
	poblacion = int(input("Rango de pares aceptados [2 , 12]:"))

maxIte = 10
vectProm = []
tempProm = 0
tempIndi = 0
### INGRESO DE DATOS ###
matSelec = genSelectionTable(tamIndividuo, poblacion)
matCruce = []
matPobla = []
for i in range(maxIte):
	print("")
	print("##### ITERACION:" , (i + 1) , "#####")
	print("** TABLA DE SELECCION **")
	printDict(matSelec)
	
	print("** TABLA DE CRUCE **")
	matCruce = genCrossingTable(matSelec)
	printDict(matCruce)

	print("** TABLA DE POBLACION **")
	matPobla = genPopulationTable(matCruce)
	printDict(matPobla)

	matSelec = matPobla
	vectProm.append(getMean(matPobla))

	if vectProm[i] > tempProm:
		tempProm = vectProm[i]
		tempIndi = i

	print("Promedio Tabla Seleccion:",getMean(matSelec))
	print("Promedio Tabla Poblacion:",getMean(matPobla))

	print("##### ITERACION:" , (i + 1) , "#####")
	
print("")
print("##### RESULTADOS #####")
print("Mejor Iteracion desde:",(tempIndi+1))
print("Promedio Poblacion:",tempProm)
print("##### RESULTADOS #####")
