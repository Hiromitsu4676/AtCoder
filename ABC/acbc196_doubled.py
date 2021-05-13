N=int(input())

count=0
for half in range(1,N):
    n=int(str(half)+str(half))
    if n>N:
        break
    else:
        count+=1
print(count)
