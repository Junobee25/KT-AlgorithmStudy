# 주어진 화폐는 한개는 무조건 쓰이고
# 주어진 화폐로 만들수있는 조합중 최솟값을 리스트에 갱신
# 리스트 인덱스는 만들 수있는 화폐
n,m = map(int,input().split())


dp = [0] * 10001

arr= []

# k원은 만들 수 있으므로 1로 초기화
for _ in range(n):
    k = int(input())
    dp[k] = 1
    arr.append(k)

# 
for i in range(len(dp)):
    k = int(1e9)
    for j in arr:
        # 최솟값 로직 
        if i > j and dp[i-j] != 0:
            if dp[i-j] <= k :
                k = dp[i-j]
    # 갱신되지 않았으면 패스
    if k == int(1e9):
        pass
    # 갱신 됬으면 최솟값 + 1
    else:
        dp[i] = k + 1
# 만들 수 없다면 -1 출력
if dp[m] == 0:
    print(-1)
else:
    print(dp[m])


