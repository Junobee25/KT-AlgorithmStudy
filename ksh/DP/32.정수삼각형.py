n = int(input())

dp = []

for i in range(n):
    dp.append(list(map(int,input().split())))
    
for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            a = 0
        else:
            a = dp[i-1][j-1] # 왼쪽 위
            
        if j == i:
            b = 0 # 위가 없음
        else :
            b = dp[i-1][j]
            
        dp[i][j] = dp[i][j] +max(a,b)
        
print(max(dp[n-1]))
            