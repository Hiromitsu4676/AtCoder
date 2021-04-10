N=int(input())
array1=list(map(int,input().split()))
array2=list(map(int,input().split()))


total_candies=set()
for i in range(N):
    up=sum(array1[:i+1])
    down=sum(array2[i:N])
    total_candies.add(up+down)

print(max(total_candies))

