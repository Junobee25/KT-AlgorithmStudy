T = int(input())
import heapq
INF = int(1e9)

dy = [-1,0,1,0]
dx = [0,1,0,-1]
for _ in range(T):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int,input().split())))

    # n*n 노드에 대한 비용 테이블
    distance = [[INF]*n for _ in range(n)]

    y,x = 0,0 # => 시작 위치
    # start 비용 위치
    q = [(graph[y][x],y,x)]
    # start 비용 초기화
    distance[y][x] = graph[y][x]
    # q가 빌 때 까지
    while q:
        # 주변 노드 중 최소 비용으로 그리디하게 갱신
        dist,y,x = heapq.heappop(q)
        # distance에는 최소비용으로 초기화 되는데 최소비용이 비용이 더 크다면 방문 처리 된것
        if distance[y][x] < dist:
            continue
        # 상하 좌우 네 방향으로 최소 비용 갱신
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny< n and 0 <= nx < n :
                cost = dist + graph[ny][nx]
                # 갱신한 비용이 갱신 된 비용 보다 작다면
                if cost < distance[ny][nx]:
                    # 최소비용 갱신
                    distance[ny][nx] = cost
                    # heqp에 넣기
                    heapq.heappush(q,(cost,ny,nx))
    print(distance[n-1][n-1])
