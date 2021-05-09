A,B,K=map(int,input().split())

n=min(A,B)
count=0
for i in range(n,0,-1):
    if A%i==0 and B%i==0:
        count +=1
    if count==K:
        rslt=i
        break

print(rslt)