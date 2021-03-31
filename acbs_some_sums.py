data=input()
data=list(map(int,data.split()))

N=data[0]
A=data[1]
B=data[2]

rslt=0
for i in range(1,N+1):
    temp=str(i)
    n=len(temp)
    
    num=0
    for j in range(n):
        num +=int(temp[j])

    if A <= num <= B:
        rslt +=i

print(rslt)
