# 화성 탐사 기계가 출발 지점에서 목표 지점까지 이동할 때 최적의 경로 찾기
# n*n크기의 2차원 공간
# [0][0] -> [N-1][N-1]
# 최단 경로 구하기 -> 다익스트라 알고리즘
import heapq
INF = int(1e9)

t = int(input())

for i in range(t):
    # 인접한 노드 확인을 위한 방향(동, 서, 남, 북)
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
        
    n = int(input())
    graph = []
    for _ in range(n):
        s = list(map(int, input().split()))
        graph.append(s)
        
    distance = [[INF]*n for _ in range(n)]
    x, y = 0, 0 # 처음 시작 위치
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]
    
    # 다익스트라 알고리즘
    while q:
        dist, x, y = heapq.heappop(q)
        
        if distance[x][y] < dist: # 이미 들린 노드
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n: # 범위 벗어난 경우
                continue
            
            cost = dist + graph[nx][ny]
            # 다른 노드를 거쳐 이동하는게 더 짧은 경우
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
                
    print(distance[n-1][n-1])