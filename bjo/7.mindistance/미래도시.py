# 문제 이해
# 한 정점에서 K번 노드를 거쳐서 X번노드를 가는데 최소비용을 구하는 문제

# 접근
# 1. 다익스트리 알고리즘 (구현 어려움)
# 한 정점에서 모든 노드로 가는데 최소 비용 구해짐
# distance => 1차원 테이블
# => 한 정점에서 X번노드로 가는 비용(1)  + X번노드에서 K번노드로 가는 비용(2)

# 2. 플로이드 워셜 알고리즘 (구현 쉬움)
# 모든 정점에서 모든 정점으로 가는데 최소비용 구할 수 있음
# distance는 2차원 테이블
# => 한 정점에서 X번노드로 가는 비용(1)  + X번노드에서 K번노드로 가는 비용(2)

n,m = map(int,input().split())
INF = int(1e9)

# 2차원 최단거리 테이블 초기화
distance = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            distance[i][j] = 0
# 그래프 만들기
for _ in range(m):
    a,b = map(int,input().split())
    distance[a][b] = 1
    distance[b][a] = 1

x,k = map(int,input().split())


# 플로이드 워셜 알고리즘
for p in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            distance[a][b] = min(distance[a][b],distance[a][p]+distance[p][b])

result = distance[1][k] + distance[k][x]

print(distance)
if result >= INF:
    print(-1)
else:
    print(result)








