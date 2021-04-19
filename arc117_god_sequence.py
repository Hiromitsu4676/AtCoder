A,B=map(int,input().split())


tempA=[i for i in range(1,A+1)]
tempB=[-j for j in range(1,B+1)]

diff=sum(tempA)+sum(tempB)

if diff>0:
    tempB[-1]=tempB[-1]-diff
elif diff<0:
    tempA[-1]=tempA[-1]-diff

rslt=tempA+tempB

print(' '.join(map(str, rslt)))