S=input()

while(1):
    ID=S[-3:]
    if len(S)==0:
        rslt='YES'
        break
    else:
        if ID=='eam':
            if S[-5:]=='dream':
                S=S[:-5]
            else:
                rslt='NO'
        elif ID=='mer':
            if S[-7:]=='dreamer':
                S=S[:-7]
            else:
                rslt='NO'
                break
        elif ID=='ase':
            if S[-5:]=='erase':
                S=S[:-5]
            else:
                rslt='NO'
                break
        elif ID=='ser':
            if S[-6:]=='eraser':
                S=S[:-6]
            else:
                rslt='NO'
                break
        else:
            rslt='NO'
            break

print(rslt)
