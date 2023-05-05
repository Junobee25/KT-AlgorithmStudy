# 다익스트라 알고리즘!!
import heapq
import sys

input = sys.stdin.readline
inf = int(1e9)

n,m,start = map(int, input().split())
graph = [[] for i in range(n+1)]

distance = [inf] * (n+1)

for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))
    
def dijkstra(start):
    q = []
    heapq.heappush(q , (0,start))
    distance[start] = 0
    while q:  # q가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist , now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q , (cost,i[0]))
            
dijkstra(start)

count = 0

max_distance = 0
for d in distance : 
    if d != inf:
        count += 1
        max_distance = max(max_distance,d)
        
print(count - 1 , max_distance)