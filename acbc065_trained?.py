N=int(input())
lights=[]
for i in range(N):
    temp=int(input())
    temp -=1
    lights.append(temp)

count=0
trained=set()
i=0
if 1 not in lights:
    rslt=-1
else:
    while(1):
        if i==1:
            rslt=count
            break
        elif i in trained:
            rslt=-1
            break
        else:
            trained.add(i)
            i=lights[i]
            count +=1  
print(rslt)
            

    