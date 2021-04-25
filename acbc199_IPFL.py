import sys
input = sys.stdin.readline

N=int(input())
S=list(input())
S.pop()
Q=int(input())
T=[list(map(int,input().split())) for _ in range(Q)]

L=len(S)
flg=0

for i in range(len(T)):
    if T[i][0]==1:
        if flg==0:
            pass
        else:
            T[i][1]=T[i][1]-N
            T[i][2]=T[i][2]-N
        temp1=S[T[i][1]-1]
        temp2=S[T[i][2]-1]
        S[T[i][1]-1]=temp2
        S[T[i][2]-1]=temp1
    else:
        flg=1-flg

temp=''.join(S)
if flg==0:
    print(temp)
else:
    print(temp[-N:]+temp[:N])