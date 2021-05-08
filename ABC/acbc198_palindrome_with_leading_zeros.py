N=str(input())
if N!='0':
    while(1):
        if N[-1] =='0':
            N=N[:-1]
        else:
            break
length=len(N)

if length==1:
    rslt='Yes'
else:
    if len(N)%2==0:
        left=N[0:int(length/2)]
        left=left[::-1]
        right=N[int(length/2):]
        if left==right:
            rslt='Yes'
        else:
            rslt='No'
    else:
        left=N[0:int(length/2)]
        left=left[::-1]
        right=N[int(length/2)+1:]
        if left==right:
            rslt='Yes'
        else:
            rslt='No'

print(rslt)
