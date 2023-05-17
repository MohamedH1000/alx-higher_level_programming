#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	square = []
	
	for row in matrix:
		b = []
		for a in row:
			b.append(a ** 2)
		square.append(b)
	return square
