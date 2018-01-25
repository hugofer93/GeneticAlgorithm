from genPairs import genPairs

def genPopulationTable(matCruce):
	ite = 0
	matPobla = []
	pareja = genPairs(len(matCruce))
	while ite < len(matCruce):
		if len(matCruce[ite]) != 0:
			padre1 = matCruce[ite].get('individuo')
			padre2 = matCruce[matCruce[ite].get('pareja')].get('individuo')
			punto = matCruce[ite].get('cruce')

			hijo1 = padre1[0:punto] + padre2[punto:len(padre2)]
			hijo2 = padre2[0:punto] + padre1[punto:len(padre2)]

			matPobla.append({'individuo':hijo1,'decimal':int(hijo1,2)})
			matPobla.append({'individuo':hijo2,'decimal':int(hijo2,2)})

			matCruce[matCruce[ite].get('pareja')].clear()
			matCruce[ite].clear()
		
		matPobla[ite]['asignacion'] = ite
		matPobla[ite]['pareja'] = pareja[ite]
		matPobla[ite]['f(x)'] = matPobla[ite].get('decimal') * matPobla[ite].get('decimal')

		ite = ite + 1

	return matPobla