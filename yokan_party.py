divide=[0,7,11,16,20,28,34,38,45]

size=[]

s=0
for i in range(1,len(divide)):
    temp=divide[i]-divide[i-1]
    size.append(temp)

print(size)

