data=input()
N,Y=map(int,data.split())

flg=False

for x in range(N+1):
    for y in range(N-x+1):
        z=N-x-y
        total=10000*x+5000*y+1000*z
        if total==Y and z>=0:
            flg=True
            break
    
    if flg==True:
        break

if flg==True:
    print(x,y,z)
else:
    print(-1,-1,-1)
