# data=input()
# N,Y=map(int,data.split())

N=1000
Y=1234000

x=-1
y=-1
z=-1

temp_x=Y/1000
temp_y=0
temp_z=0

diff=temp_x-N
flg=False

for i in range(N+1):
    if diff<0:
        break
    if diff %4==0:
        temp_y=diff/4
        temp_z=i
        temp_x=(Y-temp_y*5000-temp_z*10000)/1000
        
        if temp_x+temp_y+temp_z==N:
            flg=True
            break
        else:
            diff -=9
    else:
        diff -=9

if flg==True:
    x,y,z=temp_x,temp_y,temp_z

print(int(x),int(y),int(z))
    
    # temp_z=i
    # diff -=temp_z*9
    # temp_x=Y/1000-9*temp_z

# while diff>=0:
#     if diff %9==0:
#         temp_z= diff/9
#         if temp_z
#         rslt=True
#     else:
#         temp_y +=1
#         diff -=4

# if rslt==True:
#     x=temp_x
#     y=temp_y
#     z=temp_z

# ans=(x,y,z)
# print(ans)
        







# def func(n,remain,x,y,z):
#     if n==0:
#         if remain==0:
#             ans_x=x
#             ans_y=y
#             ans_z=z
#             return ans_x,ans_y,ans_z
#         else:
#             pass
#     else:
#         rslt=func(n-1,remain-1000,x+1,y,z) or func(n-1,remain-5000,x,y+1,z) or func(n-1,remain-10000,x,y,z+1)

# ans=


# rslt=func(N,Y,x,y,z)
# print(rslt)

    
