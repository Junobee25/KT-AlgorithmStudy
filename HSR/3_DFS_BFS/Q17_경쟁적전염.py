# n*n 시험관, 1~k 바이러스
# 매초 번호가 낮은 종류의 바이러스부터 증식

from collections import deque

n, k = map(int, input().split())
graph = []
tube = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n): # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # 바이러스의 종류, 시간, 위치(x, y) 삽입
            tube.append((graph[i][j], 0, i, j))
S, X, Y = map(int, input().split())

# 정렬 (낮은 번호의 바이러스가 먼저 증식)
tube.sort()
queue = deque(tube)

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while queue:
    virus, s, x, y, = queue.popleft()
    if s == S:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((virus, s+1, nx, ny))
                
print(graph[X-1][Y-1])
