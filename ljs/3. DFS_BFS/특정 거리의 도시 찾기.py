# 특정 거리의 도시 찾기
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

queue = deque([x])

visited = [-1] *(n+1)
visited[x] = 0

while queue:
    now = queue.popleft()
    for i in graph[now]:
        if visited[i] == -1:
            visited[i] = visited[now]+1
            queue.append(i)

flag = 0
if i in range(1, n+1):
    if visited[i] == k:
        print(i)
        flag=1
        
if flag == 0:
    print(-1)