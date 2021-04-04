N=int(input())
data=['0 0 0']
for i in range(N):
    temp=input()
    data.append(temp)

for i in range(N):
    start=list(map(int,data[i].split()))
    end=list(map(int,data[i+1].split()))

    time=end[0]-start[0]
    dis_total=abs(end[1]-start[1])+abs(end[2]-start[2])

    temp=time-dis_total
    if temp>=0 and temp%2==0:
        rslt='Yes'
    else:
        rslt='No'
        break

print(rslt)