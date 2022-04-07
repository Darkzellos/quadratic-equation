import numpy as np
print("---Квадратные уравнение---")
a = input("Введите число a: ")
b = input("Введите число b: ")
c = input("Введите число c: ")

def quadratic():
	discriminant = (pow(int(b), 2))-(4*int(a)*int(c))
	if discriminant == 0:
		x = -int(b) / 2*int(a)
		print("X = " + str(x))
	if discriminant < 0:
		print("D<0 - кореней нет")
	if discriminant > 0:
		x1 = (-int(b) + np.sqrt(int(discriminant))) / (2 * int(a))
		x2 = (-int(b) - np.sqrt(int(discriminant))) / (2 * int(a))
		print("X1 = " + str(x1) + " X2 = " + str(x2))
quadratic()