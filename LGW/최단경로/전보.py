import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
n,m = map(int, input().split())
graph = [[]for i in range(n+1)]

dist = [INF] * (n+1)

for _ in range(m):
    x,y,z =map(int,input().split())
    graph[x].append(y,z)


def hard(start):
    q = []
    heapq.heappush(q,(0,start))
    dist[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if dist[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

hard(start)

cnt = 0
max_dist = 0

for d in dist:
    if d!= INF:
        cnt +=1
        max_dist = max(max_dist,d)


print(cnt-1,max_dist)