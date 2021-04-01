N=input()
A=input()

A_list=list(map(int,A.split()))
A_list.sort()

Alice=[]
Bob=[]

while(1):
    if len(A_list)>0:
        temp=A_list.pop()
        Alice.append(temp)
        if len(A_list)==0:
            break
        else:
            temp=A_list.pop()
            Bob.append(temp)
    else:
        break

rslt=sum(Alice)-sum(Bob)

print(rslt)



