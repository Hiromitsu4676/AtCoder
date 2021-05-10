N,M=map(int,input().split())
M_list=[[] for _ in range(M)]
for i in range(M):
    temp=list(map(int,input().split()))
    M_list[i]=temp
K=int(input())
P_list=[[] for _ in range(K)]
for j in range(K):
    temp=list(map(int,input().split()))
    P_list[j]=temp

print(M_list)
print(P_list)


