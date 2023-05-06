T = int(input())
from collections import deque
# T번의 테스트 케이스
for _ in range(T):
    n,m = map(int,input().split())
    # 2차원 배열로 만들기 위해 deque형변환
    arr = deque(list(map(int,input().split())))
    # 배열 확장을 위해 deque로 형변환
    matrix = deque([[] for _ in range(n)])

    # n x m 2차원 배열로 만들기
    for i in range(n):
        for j in range(m):
            k = arr.popleft()
            matrix[i].append(k)

    # 배열 확장 로직
    # 첫번째 행
    matrix.appendleft([0]*(m+1))
    # 마지막 행
    matrix.append([0]*(m+1))

    # 배열 확장 완료
    for i in range(1,n+1):
        matrix[i].insert(0,0)

    # 다이나믹 프로그래밍 적용
    # 3 x 4 행렬
    # n = 3 // m = 4
    # n = 1,2,3 // m = 1,2,3,4
    for i in range(1,m+1):
        for j in range(1,n+1):
            matrix[j][i] = max(matrix[j-1][i-1] + matrix[j][i],
                               matrix[j][i-1] + matrix[j][i],
                               matrix[j+1][i-1] + matrix[j][i])
    max_val = -int(1e9)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
    print(max_val)