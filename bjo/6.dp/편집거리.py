# 문제 유형
# 새로운 문자열로 변환하기 위해서 필요한 삽입,제거,교체 연산의 최소 횟수

# 접근
# 부분문제(부분문자열)를 정의하고 다이나믹 프로그램을 통해 점화식을 세우면 문제를 해결 할 수 있음

A = input()
B = input()

# A의 길이 행 cat
n = len(A)
# B의 길이 열 cut
m = len(B)

# 배열 확장
matrix = [[0]*(m+1) for _ in range(n+1)]

# 기본 값은 삽입연산의 횟수로 채워줌
for i in range(n+1):
    for j in range(m+1):
        if i == 0 :
            matrix[i][j] = j
        
        if j == 0:
            matrix[i][j] = i
        
# 2차원 테이블을 그려보면 이해하기 수월함
for i in range(1,n+1):
    for j in range(1,m+1):
        if A[i-1] == B[j-1]:
            matrix[i][j] = matrix[i-1][j-1]
        else:
            matrix[i][j] = min(matrix[i-1][j],matrix[i-1][j-1],matrix[i][j-1]) + 1

        

print(matrix)


