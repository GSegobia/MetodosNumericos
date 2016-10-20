# -*- coding: utf-8 -*-
import math as math

error = 1 * 10**-8

def f(x):
	return x**3 + 3 * x - 1

def g(x):
	return x * math.log(x) - 1

def h(x):
	return x**2 - math.sin(x)

def i(x):
	return (1 + x - x**3)/4

def j(x):
	return math.exp(x)+x

def bissecao(fun, a, b, w):

	x = 0

	while abs(a-b) > w:
		x = (a+b) / 2.0
		if (fun(x)*fun(a)) < 0:
			b = x
		else:
			a = x
	return x

def falsa_posicao(fun, a, b, w):

	erro_relativo = 1.0
	x = 0.0
	y = 0.0

	while erro_relativo > w:

		x = ((a * abs(fun(b))) + (b * abs(fun(a)))) / ((abs(fun(b)) + (abs(fun(a)))))

		if fun(x) < 0.0:
			a = x
		else:
			b = x

		erro_relativo = abs(y - x)/x

		y = x

	return x

print 'Bisseção ' + str(bissecao(f, -5.0, 5.0, error))
print 'Falsa Posição ' + str(falsa_posicao(f,-5.0, 5.0, error))
print 'Bisseção ' + str(bissecao(g, 0.0001, 3.0, error))
print 'Falsa Posição ' + str(falsa_posicao(g, 0.0001, 3.0, error))
print 'Bisseção ' + str(bissecao(h, -1.0, 1.0, error))
print 'Falsa Posição ' + str(falsa_posicao(h, -1.0, 1.0, error))
print 'Bisseção ' + str(bissecao(i, -2.0, 2.0, error))
print 'Falsa Posição ' + str(falsa_posicao(i, -2.0, 2.0, error))
print 'Bisseção ' + str(bissecao(j, -1.0, 1.0, error))
print 'Falsa Posição ' + str(falsa_posicao(j, -1.0, 1.0, error))
