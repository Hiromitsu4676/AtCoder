N=input()
tempA=input()
A=tempA.split()
A=[int(x) for x in A]
count=0
while(1):
    check=0
    for i in range(len(A)):
        if A[i]%2==0:
            check+=1
            continue
        else:
            break

    if check==len(A):
        for x in range(len(A)):
            A[x]=A[x]/2
        count +=1
    else:
        break
print(count)
    

