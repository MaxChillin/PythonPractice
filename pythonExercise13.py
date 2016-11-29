#!/usr/bin/python3.5

def is_even(num1, num2):
	nums = range(num1, num2)
	evenlist = []
	for i in nums:
		if i % 2 == 0:
			evenlist.append(i)
	return evenlist

print(list(map((lambda x: x*x), is_even(4, 15))))