from genPairs import genPairs
from randomBin import randomBin

def genSelectionTable(tamIndividuo, poblacion):
	matriz = []
	pareja = genPairs(poblacion)
	for i in range(poblacion):
		individuo = ""
		
		for j in range(tamIndividuo):
			individuo = individuo + str(randomBin())
		
		decimal = int(individuo,2)
		fx = decimal * decimal

		matriz.append({'asignacion':i,'individuo':individuo,'decimal':decimal,'f(x)':fx,'pareja':pareja[i]})

	return matriz