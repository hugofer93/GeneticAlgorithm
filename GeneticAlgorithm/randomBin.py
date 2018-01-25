from numpy.random import random

def randomBin():
	num = random()
	if num >= 0.5:
		num = 1
	else:
		num = 0
	return num
