N,K=map(int,input().split())

p=1
for i in range(N):
    if i==0:
        p=p*K
    else:
        p=p*(K-1)
print(p)