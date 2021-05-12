N=int(inpt())
A=list(map(int,input().split()))

rslt=set()
for x in A:
    count=0
    temp_count=set()
    for i in range(N):
        if A[i]>=x:
            count+=x
        else:
            temp_count.add(count)
            count=0

ans=max(rslt)

print(ans)

