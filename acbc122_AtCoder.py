s=input()

temp=0
rslt=[]
for i in range(len(s)):
    if s[i] in "ACGT":
        temp+=1
    else:
        rslt.append(temp)
        temp=0
rslt.append(temp)
print(max(rslt))