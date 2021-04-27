N,L=map(int,input().split())
K=int(input())
A=list(map(int,input().split()))
 
def check_size(mid):
    global A
    global L
    global K
 
    start=0
    count=0
    for i in range(len(A)):
        if A[i]-start>=mid and L-A[i]>=mid:
            count+=1
            start=A[i]
    if count>=K:
        return True
    else:
        return False
 
left=0
right=L
 

while right-left>1:
    mid=int(left+(right-left)/2)
    if check_size(mid)==False:
        right=mid
    else:
        left=mid

print(left)