import collections
import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N=int(input())
A=list(map(int,input().split()))

a=[x%200 for x in A]

c=collections.Counter(a)
calc=[]
for x in c:
    if c[x]>=2:
        calc.append(c[x])

count=0
for n in calc:
    count +=comb(n,2)
print(count)