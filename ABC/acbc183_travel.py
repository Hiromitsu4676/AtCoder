import itertools

N,K=map(int,input().split())
T=[[] for _ in range(N)]
for i in range(N):
    T[i]=list(map(int,input().split()))

root=[n for n in range(1,N)]
permutations_lis = itertools.permutations(root)

cnt=0
for root_index in permutations_lis:
    time=0
    city=0
    for j in range(N-1):
        time+=T[city][root_index[j]]
        city=root_index[j]
    time +=T[city][0]
    if time==K:
        cnt+=1

print(cnt)
        

