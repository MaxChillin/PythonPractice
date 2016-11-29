#!/usr/bin/python3.5

def main():
	list1 = ["A", "B", "C", "D"]
	list2 = list(list1)
	list2[0] = "E"
	print(list1)
	print(list2)


main()