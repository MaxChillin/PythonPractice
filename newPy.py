#!/usr/bin/python3.5m

def main():
    filename = input("Which file? ")  
    while filename[0] != "q" and filename[0] != "Q":
        fileOpen = open(filename, "r")
        fileData = fileOpen.read().split()
        newList = []
        for string in fileData:
            newList.append(int(string))
        Square(newList)
        if everything(newList):
            print("It is a magic square.")
        filename = input("Which file? ")
    print("Done.")
    
def Square(fileData):
    i = 1
    for integer in fileData:
        print(" ", end= "")
        if integer < 10:
            print(" ", end= "")
        print(integer, end= "")
        if i % 4 == 0:
            print("\n", end= "")
        i += 1
    print("\n", end= "")
    
def Diagonal(fileData):
    l = 0
    z = 0
    p = 0
    e = 0
    for integer in fileData:
        if (z + 1) == 3:
            e += integer
        if l == z:
            p += integer
        z = (z + 1) % 4
        if z == 0:
            l += 1
    if p == 34 and e == 34:
        return True
    if p != 34:
        print("Bad diagonal sum = ", p)
    if e != 34:
        print("Bad diagonal sum = ", e)
    return False
    
def colsum(fileData, column):
    q = 0
    w = 0
    m = 0
    for integer in fileData:
        if w == column:
            m += integer
        w = (w + 1) % 4
        if w == 0:
            q += 1
    if m == 34:
        return True
    print("Bad column sum = ", m)
    return False
        
def rowsum(fileData, row):
    q = 0
    w = 0
    m = 0
    for integer in fileData:
        if q == row:
            m += integer
        w = (w + 1) % 4
        if w == 0:
            q += 1
    if m == 34:
        return True
    print("Bad column sum = ", m)
    return False

def colrowsum(fileData):
    row = 0
    column = 0
    t = True
    for integer in fileData:
        if column == 0:
            t = rowsum(fileData, row) and t
        if row == 0:
            t = colsum(fileData, column) and t
        column = (column + 1) % 4
        if column == 0:
            row += 1
    return t
    
def usedonce(fileData):
    d = []
    for integer in fileData:
        if integer in d:
            print("Not every integer used exactly once.")
            return False
        d.append(integer)
    return True
    
def everything(fileData):
    y = True
    y = colrowsum(fileData) and y
    y = Diagonal(fileData) and y
    y = usedonce(fileData) and y
    if y == True:
        return True





    
main()
