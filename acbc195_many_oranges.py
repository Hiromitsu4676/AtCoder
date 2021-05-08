import math
A,B,W=map(int,input().split())

maximum=math.floor(W*1000/A)
minmum=math.ceil(W*1000/B)

if minmum>maximum:
    print('UNSATISFIABLE')
else:
    print(minmum,maximum)