S=input()

for bit in range(1 << 3):
    ans=int(S[0])
    f=S[0]
 
    for i in range(3):
        if bit&(1 << i):
            ans += int(S[i+1])
            f += "+"
        else:
            ans -= int(S[i+1])
            f += "-"
        f += S[i+1]
    if ans == 7:
        print(f + "=7")
        break
