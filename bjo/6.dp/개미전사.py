# 문제 이해
# 최소한 한 칸 이상 떨어진 인덱스의 요소들을 합하여 나감
# 최댓값 구하기

# 점화식 dp[n] = (dp[n-3] + dp[n]),(dp[n-2]+dp[n]) 중 최댓값

n = int(input())
dp = list(map(int,input().split()))

dp[2] = dp[0] + dp[2]

for i in range(3,len(dp)):
    dp[i] = max((dp[i-2] + dp[i]),(dp[i-3] + dp[i]))


print(max(dp[i-1],dp[i]))