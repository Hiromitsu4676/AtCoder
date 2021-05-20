import math
N,M=map(int,input().split())
A=list(map(int,input().split()))

white=[]
if M==0:
    rslt=1
else:
    A.append(N+1)
    A.sort()
    w=A[0]-1
    if w!=0:
        white.append(w)

for i in range(1,len(A)):
    w=A[i]-A[i-1]-1
    if w!=0:
        white.append(w)

if M!=0:
    if len(white)==0:
        rslt=0
    else:
        k=min(white)

        rslt=0
        for num in white:
            temp=math.ceil(num/k)
            rslt+=temp

print(rslt)



