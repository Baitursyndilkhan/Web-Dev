import math

def doublePow(a,b):
    return math.pow(a,b)

a,b = input().split()
a = float(a)
b  = int(b)

print(doublePow(a,b))
