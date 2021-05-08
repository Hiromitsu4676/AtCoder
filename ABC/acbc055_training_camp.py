N=int(input())
power=1
mod=10**9+7
surplus=power%mod
for i in range(1,N+1):
    surplus=surplus*i%mod
print(surplus)

