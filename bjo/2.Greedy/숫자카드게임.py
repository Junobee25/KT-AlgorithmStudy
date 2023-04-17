# 문제 이해
# 행의 최소 값들 중에서 가장 큰 최솟값을 구하는 문제

N,M = list(map(int,input().split()))
matrix = []
result = 0
for _ in range(N):
    matrix.append(list(map(int,input().split())))
    # 가장 최솟 값
    min_value =  min(matrix)
    # 최솟 값 중에서 큰 값
    result = max(min_value,result)
print(result)