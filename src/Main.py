from array import array
import re 
def CreateRange():
    x= input()

    y =[i for i in re.split('(-?\d+\.?\d*)',x)if i !='']
    print(y)
    range = [int(m) for m in x.isdigit()]
    if y[0] == '(':
        v1 = y[1] + 1 
    if y[-1] == ')':
        v2 = y[3] + 1

    return v1, v2



def integer_range_contains(range, val):
    for i in range:
        if range[i] in val:
            return True
        else:
            return False
    

def getAllPoint(range):
    return range

def ContainsRange(range1, range2):
    max1 = max(range1)
    max2 = max(range2)
    min1 = min(range1)
    min2 = min(range2)
    if max2 > max1 or min2<min1:
        return False
    else :
        return True
    

def endPoints(range):
    max1 = max(range)
    min1 = min(range)
    val = [min1 , max1]
    return val

def Equals(range1, range2):
    if range1 == range2:
        return True
    else:
        return False

def overlapsRange():
    return