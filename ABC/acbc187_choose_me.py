N=int(input())
A=[]
B=[]
Diff=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
    Diff.append(2*a+b)

aoki=sum(A)
diff=0

C.sort()
cnt=0

for j in range(N):
    diff +=Diff.pop()
    cnt +=1
    if diff>aoki:
        break

print(cnt)
