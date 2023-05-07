for tc in range(int(input())):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))

    dp =[]
    idx =0
    for i in range(n):
        dp.append(arr[idx:idx+m])
        idx+=m

    for i in range(1,m):
        for j in range(n):
            if j == 0:
                left_up = 0

            else :
                left_up = dp[j-1][i-1] 
            if i == n-1:
                left_down = 0
            else :
                left_down = dp[j+1][i+1]
            left = dp[j][i-1]
            dp[j][i]=dp[j][i] + max(left_up,left_down,left)
result = 0
for i in range(n):
    result = max(result,dp[i][m-1])
print(result)
    