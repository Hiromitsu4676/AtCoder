A,B,C,D=list(map(int,input().split()))

A_on=[]
B_on=[]
for i in range(A,B+1):
    A_on.append(i)
for i in range(C,D+1):
    B_on.append(i)

match=[]
for a in A_on:
    if a in B_on:
        match.append(a)

if len(match)==0:
    ans=0
else:
    ans=len(match)-1
print(ans)

