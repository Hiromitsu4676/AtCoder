N=int(input())
d=[None]*N
for i in range(N):
    d[i]=int(input())

d.sort()
kagami_mochi=[None]
for i in range(N):
    temp=d.pop()
    if temp!=kagami_mochi[-1]:
        kagami_mochi.append(temp)

rslt=len(kagami_mochi)-1
print(rslt)
    
