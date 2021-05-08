N=8
S='WWWWWEEE'

W_CUSUM=[0]
E_CUSUM=[0]
W=0
E=0
for i in range(N):
    if S[i]=='W':
        W+=1
    if S[i]=='E':
        E+=1
    W_CUSUM.append(W)
    E_CUSUM.append(E)

print(W_CUSUM)
print(E_CUSUM)

attention=[]
for i in range(N):
    left=W_CUSUM[i]
    right=E_CUSUM[N]-E_CUSUM[i+1]
    attention.append(left+right)

print(attention)
print(min(attention))
