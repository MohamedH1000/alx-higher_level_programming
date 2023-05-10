#!/usr/bin/python3
def pow(a, b):
	r = 1
	n = 0
	bs = 1

	if b < 0:
		n = b
		b = (-1) * b

	for x in range(b):
		r *= a
		bs = r * r

	if n  < 0:
		r /= bs
	return r
