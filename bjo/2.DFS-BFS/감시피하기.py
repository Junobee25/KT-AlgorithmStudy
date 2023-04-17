from itertools import combinations
import copy

# N*N
n = int(input())
# 복도
matrix = []
for i in range(n):
    k = list(input().split())
    matrix.append(k)

# 빈칸의 좌표를 모두 찾아서 (y,x) 이렇게 저장 => 위치
com = [(y,x) for x in range(n) for y in range(n) if matrix[y][x] == 'X']
# 모든 경우의 찾기! => N*N칸 빈칸 3개를 택해서 벽을 세우는 경우의 수를 리스트로 표현
combi = list(combinations(com,3)) 

# 4가지 방향에 대한 벡터
dy = [-1,0,1,0]
dx = [0,1,0,-1]

# 선생의 감시를 피할 수 있는지
def check(y,x,matrix):
    for _ in range(1):
        for i in range(4):
            # 선생님 나왔는데 주변만 탐색하는게 아니라 쭉 탐색해야 되요 ==> 선생님은 복도끝까지 볼 수 있다. 
            for j in range(1,n+1): 
                ny = y + dy[i]*j
                nx = x + dx[i]*j
                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    break
                if matrix[ny][nx] == 'O':
                    break
                if matrix[ny][nx] == 'S': # 학생을 만난다 
                    return False 
    return True


# 브루트 포스
for c in combi: 
    #[((벽1)(벽2)(벽3))]
    set_map = copy.deepcopy(matrix)
    set_map[c[0][0]][c[0][1]] = 'O'
    set_map[c[1][0]][c[1][1]] = 'O'
    set_map[c[2][0]][c[2][1]] = 'O'

    answer = 'YES'

    for y in range(n):
        for x in range(n):
            # n*n에서 선생님이 나왔다
            if set_map[y][x] == 'T':
                if not check(y,x,set_map):
                    answer = 'NO'

    if answer == 'YES':
        break
print(answer)


