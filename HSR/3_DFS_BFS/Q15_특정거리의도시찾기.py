# 도시 n개, m개의 단방향 도로, 출발도시 x
# 최단거리가 k인 도시만 출력

# 최단거리 문제, BFS => 모든 도로의 길이가 1이기 때문
from collections import deque

n, m, k, x = map(int, input().split())
city = [[]for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    city[a].append(b)
    
distance = [-1]*(n+1)
distance[x] = 0

queue = deque([x])
while queue:
    a = queue.popleft()
    
    for i in city[a]:
        if distance[i] == -1:
            distance[i] = distance[a]+1
            queue.append(i)
            
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
        
if check == False:
    print(-1)