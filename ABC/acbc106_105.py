N=int(input())
k=int(N/2)
count=0
for n in range(k+1):
    temp=0
    odd=2*n+1
    for i in range(1,N+1):
        if odd%i==0:
            temp+=1
    if temp==8:
        count+=1
print(count)

# if N>=195:
#     print(5)
# elif N>=189:
#     print(4)
# elif N>=165:
#     print(3)
# elif N>=135:
#     print(2)
# elif N>=105:
#     print(1)
# else:
#     print(0)