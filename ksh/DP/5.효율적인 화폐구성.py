import sys

n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [float('inf')] * (m+1)
dp[0] = 0

for i in range(1, m+1):
    for coin in coins:
        if i >= coin:
            dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[m] == float('inf'):
    print(-1)
else:
    print(dp[m])