import sys
sys.setrecursionlimit(10000)

S=input()
W=None

def rec(s,w):
    if len(s)==0:
        return True

    if w=='dream':
        if s[:5]==w:
            s=s[5:]
        else:
            return False
    if w=='erase':
        if s[:5]==w:
            s=s[5:]
        else:
            return False  
    if w=='eraser':
        if s[:6]==w:
            s=s[6:]
        else:
            return False  
    if w=='dreamer':
        if s[:7]==w:
            s=s[7:]
        else:
            return False      

    
    rslt=rec(s,'dream') or rec(s,'dreamer') or rec(s,'erase') or rec(s,'eraser')
    
    return rslt

ans=rec(S,W)

if ans==True:
    print('YES')
else:
    print('NO')
