N,K=map(int,input().split())
F=[[] for _ in range(N)]
for i in range(N):
    F[i]=list(map(int,input().split()))
F[i].sort()
vil=0

while K>0:
    temp=[]
    get=0
    if len(F)>0:
        for j in range(len(F)):
            if F[j][0]<=K+vil:
                get += F[j][1]
            else:
                temp.append(F[j])
    vil +=K
    K=get
    F=temp
        
print(vil)