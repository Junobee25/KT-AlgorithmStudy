n = int(input())
array =list(map(int, input().split()))

array.reverse()

dp = [1]*n


for i in range(1,n): # index 1 부터 n-1 까지
    for j in range(0,i): # index 0 부터 i까지 비교(0~1 ,0~2 ,0~3, 0~4 ....)
        if array[j] < array[i]: # 비교 대상 index가 i index보다 작을 경우
            dp[i] = max(dp[i] , dp[j] + 1) # j 번째가 i 번째 보다 작을 경우 i 번째 dp에 j 번째 dp의 수 더하기 1 해준다.
            # 최종적으로 가장 큰 수는 연속수의 가장 큰 값이 들어가 있을 것이다 .
            
print(n - max(dp))

# 가장 긴 증가하는 부분 수열 이란 하나의 수열이 주어졌을 때 값들이 증가하는 형태의 가장 긴 부분 수열을 찾는 문제이다

# 점화식 : DP[i] 를 모두 1로 초기화

# 이 문제에서는 큰 수가 앞에 오므로 REVERSE() 사용 해서 오름차순으로 바꿔주고 LIS ALGORITHM 사용 

