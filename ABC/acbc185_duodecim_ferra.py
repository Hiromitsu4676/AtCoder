import math
def cmb(n,r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))


L=int(input())

rslt=cmb(L-1,11)
print(rslt)