import re
vals=input()
a,b=re.split(" ",vals)
if (int(a)*int(b))%2==0:
    print("Even")
else:
    print("Odd")