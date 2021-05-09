N=int(input())
n=int(N**0.5)

L=set()
for i in range(1,n+1):
    if N%i==0:
        L.add(i)
a=max(L)
b=int(N/a)

temp=max(a,b)
rslt=len(str(temp))

print(rslt)