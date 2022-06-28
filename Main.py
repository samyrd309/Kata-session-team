import re
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



    