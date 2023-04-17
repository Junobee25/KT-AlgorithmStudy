from collections import deque

# 처음 방문하는 노드에만 그 전 노드에 1을 더해주면 최솟값이 갱신될 것이다.

n,m = map(int,input().split())
miro = []

for _ in range(n):
    miro.append(list(map(int,input())))

dy = [-1,0,1,0]
dx = [0,1,0,-1]
# 1인 요소만 더해줄꺼기 때문에 방문리스트 필요없음
def bfs(y,x):
    q = deque()
    q.append([y,x])
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m and miro[ny][nx] == 1:
                # 부모노드에 + 1 하며 탐색하기
                miro[ny][nx] = miro[y][x] + 1
                q.append([ny,nx])
    return miro[n-1][m-1] # 마지막 요소에는 최솟값이 들어있음
                
print(bfs(0,0))