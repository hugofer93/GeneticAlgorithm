def getMean(mat):
	promedio = 0
	for i in range(len(mat)):
		promedio = promedio + mat[i].get('f(x)')

	promedio = promedio / (len(mat))
	return (round(promedio,2))