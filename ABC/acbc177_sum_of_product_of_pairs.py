N=int(input())
A=list(map(int,input().split()))
S=[0]
temp=0
for i in range(N):
    temp +=A[i]
    S.append(temp)
mod=10**9+7
rslt=0
for k in range(N-1):
    n=(A[k]*(S[-1]-S[k+1]))%mod
    rslt+=n

rslt=rslt%mod
print(rslt)
