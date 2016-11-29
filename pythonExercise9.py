#!/usr/bin/python3.5

def main():
	result = cents(input("Enter A number: "))
	print(result)


def cents(number):
	return int(int(number) / 100)

main()