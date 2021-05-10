A,B,C,X,Y=map(int,input().split())

a=X
b=Y
c=0

Cost=[A*a+B*b]
N=max(a,b)
for i in range(N):
    c+=2
    a-=1
    b-=1
    if a<=0:a=0
    if b<=0:b=0
    price=A*a+B*b+C*c
    Cost.append(price)

rslt=min(Cost)

print(rslt)
