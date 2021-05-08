n,k,m=map(int,input().split())
a=list(map(int,input().split()))

total=sum(a)
target=m*n

if target-total<=k:
    rslt=target-total
    if rslt<0:rslt=0
else:
    rslt=-1

print(rslt)