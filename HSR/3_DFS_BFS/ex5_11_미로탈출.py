# n*m 직사각형 형태의 미로
# 0 : 괴물이 있는 부분, 1 : 괴물이 없는 부분

# bfs : 한 노드에서 최단 거리의 노드 확인
from collections import deque

n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))
    
# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

queue = deque()
queue.append((0, 0)) # 첫 시작 좌표

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        # 범위 벗어날 경우 무시
        if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
            continue
        
        # 괴물이 있을 경우 무시
        if maze[nx][ny] == 0:
            continue
        
        # 괴물이 없을 경우
        if maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            queue.append((nx, ny))
            
print(maze[n-1][m-1])