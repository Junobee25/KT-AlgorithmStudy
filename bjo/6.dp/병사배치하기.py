# 문제 유형
# 가장 긴 감소하는 수열을 찾는 문제

# 접근
# 가장 긴 감소하는 수열의 길이를
# 각 원소마다 1로 두고
# 갱신된 이전의 값 중
# 자기자신 보다 크고 길이가 최대인 요소를 선택하여
# 현재 길이에 더해줌

n = int(input())
arr = list(map(int,input().split()))

# 초기 길이 1로 초기화
dp = [1]*n

# 시작 길이는 1이니 인덱스 1부터 시작
for i in range(1,n):
    # 최장증가 수열 길이 초기화
    max_len = -int(1e9)
    # 이전의 값들을 비교
    for j in range(i):
        # 이전의 값 중 현재 값보다 큰수에 대해서
        if arr[j] > arr[i]:
            # 최장길이가 현재 길이보다 작으면
            if max_len  < dp[j]:
                # 최장 길이를 초기화
                max_len = dp[j]
    # 초기화 되지 않았으면 그대로 두기
    if max_len == -int(1e9):
        pass
    # 최대로 초기화 되있으면 현재길이에서 최장거리 더하기
    else:
        dp[i] += max_len


print(n-max(dp))