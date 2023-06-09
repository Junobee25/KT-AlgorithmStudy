# 문제 유형
# 다이나믹 프로그래밍
# 2,3,5만을 소인수로 가지는 수를 오름차순으로 나열했을 때
# k 번째 수를 구하는 문제

# 접근
# 모든요소가 0인 1001길이의 배열 선언
# 인덱스를 못생긴 수로 설정한다.
# 못생긴 수면 1 아니면 0 으로 할당되도록 로직구현할것
# 인덱스를 탐색하면서 2 or 3 or 5로 나누었을 때 값이 못생긴 수 이면 그 값도 못생긴수
# flag를 먼저 false로 설정하면 위 조건을 만족하면 현재 인덱스를 1로 바꿈
# 오름차순으로 나열하기 위해 1인 요소들만 새로운 배열에 append
# 새로운 배열은 못생긴 수들로만 이루어져있고 k번째 인덱스의 값이 문제에서 구해야하는 답

n = int(input())
dp = [0]*1001
dp[1],dp[2],dp[3],dp[5] = 1,1,1,1

# 4번부터 탐색하면 됨
for i in range(4,len(dp)):
    # 나누려는 값이 정수일때만 인덱스로 쓸수있음
    # 아래의 3가지 조건중 하나라도 만족하면 그 수 는 못생긴 수가 될 수 있음
    # 왜냐하면 못생긴 수에서 2,3,5를 곱한 값은 못생긴 수 이므로
    if i%2 == 0 and dp[i//2] == 1:
        dp[i] = 1
    elif i%3 == 0 and dp[i//3] == 1:
        dp[i] = 1
    elif i%5 == 0 and dp[i//5] == 1:
        dp[i] = 1
ugly_num = []
for i in range(len(dp)):
    if dp[i] == 1:
        ugly_num.append(i)
print(ugly_num)

