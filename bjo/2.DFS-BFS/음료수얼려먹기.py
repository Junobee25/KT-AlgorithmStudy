# Access
# 구역 분할 문제 
# bfs로 상하좌우 탐색하며 더 이상 갈수 없으면 아이스크림 추가하고 bfs 반복
# 모두 방문처리되고 갈수없는 경우일 때까지 bfs 돌기


from collections import deque
n,m = map(int,input().split())

# 입력
board = []
visited = [[False]*m for _ in range(n)]
for _ in range(n):
    board.append(list(map(int,input())))

# 방향 벡터 설정
dy = [-1,0,1,0]
dx = [0,1,0,-1]
answer = 0

# bfs 구현
def bfs(y,x):
    q = deque()
    q.append([y,x])
    visited[y][x] = True
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m and visited[ny][nx] == False and board[ny][nx] == 0:
                visited[ny][nx] = True
                q.append([ny,nx])
                

# 노드마다 bfs 호출
for i in range(n):
    for j in range(m):
        # 방문처리 x 0인 경우만 bfs 호출
        if visited[i][j] != True and board[i][j] == 0:
            bfs(i,j)
            answer += 1
print(answer)