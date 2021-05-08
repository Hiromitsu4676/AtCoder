N=int(input())

rslt='No'

for n in range(1,10):
    for m in range(1,10):
        if n*m==N:
            rslt='Yes'
            break
    if rslt=='Yes':
        break


print(rslt)
