# 문제 이해
# 바이러스가 매초 마다 증식하는데
# 번호가 작은 바이러스 부터 증식
# 이미 바이러스가 증식된 칸은 증식할 수 없음
# S초 후에 x,y좌표의 바이러스 번호 출력 없으면 0출력

# 접근
# 리스트에 바이러스 종류를 담고 정렬 (중복x)
# 최솟값부터 bfs돈다.

from collections import deque

n, k = map(int,input().split())
matrix = []
for i in range(n):
    k = list(map(int,input().split()))
    matrix.append(k)

s,x,y = map(int,input().split())

virus = []
# 바이러스 정보를 리스트에 담기
for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0:
            virus.append((matrix[i][j],i,j))
# 작은값 부터 비교해야 하기 때문에 정렬
virus.sort()

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def bfs(s,y,x):
    cnt = 0
    q = deque(virus)
    while q:
        if cnt == s:
            break
        # 바이러스 순서대로 전파하면서 1초 카운트
        for _ in range(len(q)):
            pred,ny,nx = q.popleft()
            for i in range(4):
                py = ny + dy[i]
                px = nx + dx[i]
                if 0<= py < n and 0<= px < n and matrix[py][px] == 0:
                    matrix[py][px] = matrix[ny][nx]
                    q.append((matrix[py][px],py,px)) # 증식 후 바이러스 종류 위치
        cnt += 1
    return matrix[y-1][x-1]
print(bfs(s,x,y))