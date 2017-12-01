# Компьютерный практикум 2 (NOD)
# Напишите программу, которая реализует нахождение наибольшего общего делителя двух чисел A, B
# Тесты оформите с помощью pytest или UnitTest.

import pytest
import nod

def fact(a, b, c):
	def test():
		assert nod.nod(a, b) == c
	return test


test1 = fact(1, 11, 1)
test2 = fact(5, 55, 5)
test3 = fact(12345, 123, 3)