n=int(input())
price=[]
for i in range(n):
    price.append(int(input()))
dp=[0 for i in range(n)]
dp[1]=price[1]
for i in range(2,n):
    dp[i]=min(dp[i-1],dp[i-2])+price[i]
print(dp[n-1])

