N=int(input())
count=0
if N>=10000:
    if N>=100000:N=99999
    count+=(N-10000+1)
    count+=900
    count+=9
elif N>=100:
    if N>=1000:N=999
    count+=(N-100+1)
    count+=9
else:
    if N>=10:N=9
    count+=N

print(count)