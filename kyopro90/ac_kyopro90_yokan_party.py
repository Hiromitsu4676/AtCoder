N,L=map(int,input().split())
K=int(input())
A=list(map(int,input().split()))

def check_size(target):
    global A
    global L
    global K

    start=0
    count=0
    for i in range(len(A)):
        if A[i]-start>=target and L-A[i]>=target:
            count+=1
            start=A[i]
    if count>=K:
        return True
    else:
        return False

left=0
right=L/(K+1)

OK=set()
NG=set()

while(1):
    center=int((left+right)/2)
    if check_size(center)==True:
        OK.add(center)
        left=center
        if center+1 in NG:
            rslt=center
            break
    else:
        NG.add(center)
        right=center
        if center-1 in OK:
            rslt=center-1
            break
    
print(rslt)
