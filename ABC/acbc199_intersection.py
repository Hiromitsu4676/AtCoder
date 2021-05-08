N=int(input())
A=tuple(map(int,input().split()))
B=tuple(map(int,input().split()))

rslt=min(B)-max(A)+1

if rslt<0:
    print(0)
else:
    print(rslt)
