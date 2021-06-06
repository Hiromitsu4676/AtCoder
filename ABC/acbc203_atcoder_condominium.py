n,k=map(int,input().split())

rslt=0
for i in range(1,n+1):
    for j in range(1,k+1):
        rslt +=100*i+j

print(rslt)