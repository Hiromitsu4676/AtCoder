import re
a=input()
bc=input()
s=input()

b,c=re.split(" ",bc)

print(int(a)+int(b)+int(c),str(s))