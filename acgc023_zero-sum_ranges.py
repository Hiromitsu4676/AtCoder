import collections
import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N=int(input())
A=list(map(int,input().split()))

CUSUM=[0]
temp=0
for i in range(N):
    temp+=A[i]
    CUSUM.append(temp)

c=collections.Counter(CUSUM)
calc=[]
for x in c:
    if c[x]>=2:
        calc.append(c[x])

count=0
for n in calc:
    count +=comb(n,2)

print(count)
    

