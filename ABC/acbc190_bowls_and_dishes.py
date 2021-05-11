import itertools

N,M=map(int,input().split())
condi=[[] for _ in range(M)]
for i in range(M):
    temp=list(map(int,input().split()))
    condi[i]=temp
K=int(input())
choice=[[] for _ in range(K)]
for j in range(K):
    temp=list(map(int,input().split()))
    choice[j]=temp

rslt=0

for balls in itertools.product(*choice):
    count=0
    for a,b in condi:
        if a in balls and b in balls:
            count+=1
    if count>rslt:
        rslt=count

print(rslt)
