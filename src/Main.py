from array import array
import re 
def CreateRange(x):
    y =[i for i in re.split('(-?\d+\.?\d*)',x) if i !='']
    print(y)
    range = [int(m) for m in y if m.isdigit]
    if y[0] == '(':
        v1 = range[0] + 1
    if y[-1] == ']':
        v2 = range[1] + 1
    output=[v1,v2]
    return output 



def integer_range_contains(defaultrange, inputrange):
    defaultrange = [i for i in range(defaultrange[0], defaultrange[1])]
    for i in defaultrange:
        if defaultrange[i] in inputrange:
            return True
        else:
            return False
    

def getAllPoint(inputrange):
    return [i for i in range(inputrange[0], inputrange[1])]

def ContainsRange(arr1, arr2):
    arr1 = [i for i in range(arr1[0], arr1[1])]
    arr2 = [i for i in range(arr2[0], arr1[1])]
    if max(arr2) > max(arr1) or min(arr2)<min(arr1):
        return False
    else :
        return True
    

def endPoints(inputrange):
    x = [i for i in range(inputrange[0], inputrange[1])]
    valMax = max(x)
    valMin = min(x)
    return valMax, valMin

def Equals(inputrange1, inputrange2):
    arr1 = [i for i in range(inputrange1[0], inputrange1[1])]
    arr2 = [i for i in range(inputrange2[0], inputrange2[1])]
    if arr1 == arr2:
        return True
    else:
        return False

