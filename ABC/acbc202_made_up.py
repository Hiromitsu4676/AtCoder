import collections

N=int(input())
A=tuple(map(int,input().split()))
B=tuple(map(int,input().split()))
C=tuple(map(int,input().split()))

B_=[]
for i in range(N):
    index=C[i]-1
    B_.append(B[index])

B_count=collections.Counter(B_)

cnt=0
for j in range(N):
    if A[j] in B_count:
        cnt +=B_count[A[j]]

print(cnt)
