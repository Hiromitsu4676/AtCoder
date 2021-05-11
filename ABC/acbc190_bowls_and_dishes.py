N,M=map(int,input().split())
M_list=[[] for _ in range(M)]
for i in range(M):
    temp=list(map(int,input().split()))
    M_list[i]=temp
K=int(input())
P_list=[[] for _ in range(K)]
for j in range(K):
    temp=list(map(int,input().split()))
    P_list[j]=temp

print(M_list)
print(P_list)

#標準入力
n, m = map(int,input().split())

A = []
B = []
for i in range(m):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)

k = int(input())

C = []
D = []
for i in range(k):
    c, d = map(int,input().split())
    C.append(c)
    D.append(d)

# 満たした条件
ans = 0

#bit全探索(2^k回繰り返す)
#人iがCの皿をおいたかDの皿をおいたかを二進数表記にする
#0101ならCDCDを選んだ、と考える


for num in range(2 ** k):
    
    dish = [0] * n
    #皿の上のボールの数を格納するリスト。初期はすべてゼロ

    for j in range(k):
        '''
        numがのとき二進数表記で0101
        0回シフトすると：0101
        1回シフトすると：0010
        2回シフトすると：0001
        '''
        bit=bin(num)
        if (num >> j) & 1:
            #J番目が1ならばDのボールをおく
            dish[D[j]-1] += 1
        else:
            #J番目が0ならばCのボールをおく
            dish[C[j]-1] += 1

    sum_i = 0
    for l in range(m):
        if dish[A[l]-1] > 0 and dish[B[l]-1] > 0:
            sum_i += 1

    if ans < sum_i:
        ans = sum_i
else:
    print(ans)
