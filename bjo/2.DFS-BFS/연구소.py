# 문제 이해
# 연구소의 크기는 NxM 빈칸,벽으로 구성
# 일부 칸은 바이러스가 존재, 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있음.
# 세울 수 있는 벽의 개수는 무조건 3개
# 벽을 잘 세워서 바이러스가 퍼지지 않게 되는 안전영역의 최대 수


# 접근
# 주어진 영역안 빈칸 중 3개를 택하는 경우를 모두 고려한다.
# 택해진 영역에 대해서 바이러스가 퍼진 후 남아있는 안전영역의 개수를 구해본다.\
# 8x8에서 64C3 === 42000 * 8*8 가능할 듯

from itertools import combinations
from collections import deque
import copy

n, m = map(int,input().split())

laboratory = []

# 연구소 만들기
for i in range(n):
    k = list(map(int,input().split()))
    laboratory.append(k)

blank = []
# 빈칸 위치 blank 저장
for i in range(n):
    for j in range(m):
        if laboratory[i][j] == 0:
            blank.append((i,j))

# 방향
dy = [-1,0,1,0]
dx = [0,1,0,-1]

# 바이러스 전파 bfs 함수
def bfs(y,x):
    q = deque()
    q.append((y,x))
    while q:
        ny,nx = q.popleft()
        for i in range(4):
            py = ny + dy[i]
            px = nx + dx[i]
            if 0 <= py < n and 0 <= px < m and result_arr[py][px] == 0:
                result_arr[py][px] = 2
                q.append((py,px))

result = 0      
# 조합 => comb 따라 bfs를 돌려 바이러스를 전파 후 안전영역의 갯수(cnt)를 최댓값으로 계속 갱신
for i in combinations(blank,3):
    cnt = 0
    result_arr = copy.deepcopy(laboratory) # cobi에 따른 상황 갱신
    for y,x in i:
        result_arr[y][x] = 1 # 벽 설치

    for i in range(n): # 바이러스 전파
        for j in range(m):
            if result_arr[i][j] == 2:
                bfs(i,j)

    for a in range(n): # 안전영역 개수 찾기
        for b in range(m):
            if result_arr[a][b] == 0:
                cnt += 1

    if result < cnt : # 최댓값 갱신
        result = cnt

print(result)

# bfs로직이 틀린거 같은데 뭐가 잘못된건지 생각중..



    






