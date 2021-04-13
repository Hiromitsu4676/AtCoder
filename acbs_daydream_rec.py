'''
未完成
'''


S=input()

def rec(s,w):
    if len(s)==0:
        return True

    if len(w)==5:
        if s[:5]=='dream' or 'erase':
            s=s[5:]
        else:
            return False
    if len(w)==6:
        if s[:6]=='eraser':
            s=s[6:]
        else:
            return False
    if len(w)==7:
        if s[:7]=='dreamer':
            s=s[7:]
        else:
            return False
    
    rslt=rec(s,'dream') or rec(s,'dreamer') or rec(s,'erase') or rec(s,'eraser')
    
    return rslt

ans=rec(S,'')

print(ans)
