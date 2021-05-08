import math
R,X,Y=list(map(int,input().split()))

distance=math.sqrt(X**2+Y**2)

if distance==R:
    step=1
elif distance<=2*R:
    step=2
else:
    step=math.ceil(distance/R)

print(step)
    


    


