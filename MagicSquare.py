#!/usr/bin/python3.5
from sys import exit

def main():
    while True:
        filename = input("Enter the file name: ")
        if filename[0] == "q" or filename[0] == "Q":
            print("Done.")
            exit()
        file = open(filename)
        for line in file:
            numList = line.split(" ")
        
        printNumbers(numList)
        testForMagic(numList)

            
def testForMagic(args):
    flag = testRow1(args)
    flag = testRow2(args) and flag
    flag = testRow3(args) and flag
    flag = testRow4(args) and flag
    flag = diagonalTest1(args) and flag
    flag = diagonalTest2(args) and flag 
    flag = integerUsage(args) and flag
    if flag:
        print("It is a Magic Square!")


def printNumbers(args):
    index = 1
    for i in args:
        i = int(i)
        if i < 10:
            print(" " + str(i) + " ", end='')
        else:
            print(str(i) + " ", end='')
        if (index % 4) == 0:
            print()
        index += 1;
    
def diagonalTest1(args):
    index = 0
    total = 0
    for i in args:
        if (index % 5) == 0:
            total += int(i)
        index += 1;
    
    if total == 34:
        return True
    else:
        print("Bad diagonal sum = ", total)
        return False
    
    
def diagonalTest2(args):
    index = 0
    total = 0
    for i in args:
        if index != 0 and (index % 3) == 0 and index != 15:
            total += int(i)
        index += 1;
    
    if total == 34:
        return True
    else:
        print("Bad diagonal sum = ", total)
        return False
    
    
def integerUsage(args):
    seen = set()
    for i in args:
        if i in seen or i not in [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ]:
            print("Not every integer used exactly once.")
            return False
        seen.add(i)
    return True
    
    
def testRow1(args):
    index = 0
    total = 0
    for i in args:
        if index < 4:
            total += int(i)
        index += 1;
    
    if total == 34:
        return True
    else:
        print("Bad row sum = ", total)
        return False
    
def testRow2(args):
    index = 0
    total = 0
    for i in args:
        if index > 3 and index < 8:
            total += int(i)
        index += 1;
    
    if total == 34:
        return True
    else:
        print("Bad row sum = ", total)
        return False
    
    
def testRow3(args):
    index = 0
    total = 0
    for i in args:
        if index > 7 and index < 12:
            total += int(i)
        index += 1;
    
    if total == 34:
        return True
    else:
        print("Bad row sum = ", total)
        return False
    
    
def testRow4(args):
    index = 0
    total = 0
    for i in args:
        if index > 11 and index < 16:
            total += int(i)
        index += 1;
    
    if total == 34:
        return True
    else:
        print("Bad row sum = ", total)
        return False
    
main()

