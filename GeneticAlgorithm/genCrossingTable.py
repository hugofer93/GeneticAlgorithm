from genPairs import genPairs
from numpy.random import random

def genCrossingTable(matSelec):
	ite = 0
	matCruce = []
	individuo1 = ""
	individuo2 = ""
	pareja = genPairs(len(matSelec))
	while ite < len(matSelec):
		
		if len(matSelec[ite]) != 0:
			individuo1 = matSelec[ite].get("individuo")
			individuo2 = matSelec[matSelec[ite].get("pareja")].get("individuo")
			cruce = int((len(individuo1) - 1) * random() + 1)
			
			if int(individuo1,2) >= int(individuo2,2):
				matCruce.append({'individuo':individuo1,'decimal':int(individuo1,2),'cruce':cruce})
				matCruce.append({'individuo':individuo1,'decimal':int(individuo1,2),'cruce':cruce})
			else:
				matCruce.append({'individuo':individuo2,'decimal':int(individuo2,2),'cruce':cruce})
				matCruce.append({'individuo':individuo2,'decimal':int(individuo2,2),'cruce':cruce})

			matSelec[matSelec[ite].get("pareja")].clear()
			matSelec[ite].clear()

		matCruce[ite]['asignacion'] = ite
		matCruce[ite]['pareja'] = pareja[ite]

		ite = ite + 1
	return matCruce