'''
未完成
'''


S=input()

def rec(s):
    if len(s)==0:
        return True
    else:
        if s[0:5]=='dream':
            rslt=rec(s[5:])
        elif s[0:7]=='dreamer':
            rslt=rec(s[7:])
        elif s[0:5]=='erase':
            rslt=rec(s[5:])
        elif s[0:6]=='eraser':
            rslt=rec(s[6:])
        else:
            return False
        
rslt=rec(S)
print(rslt)