A,B,C=map(int,input().split())

remaining=[]
for i in range(1,B+1):
    temp=A*i%B
    remaining.append(temp)
if C in remaining:
    rslt='Yes'
else:
    rslt='No'

print(rslt)


