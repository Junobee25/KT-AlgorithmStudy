# n개의 행성, 3차원 좌표 위의 한 점
# 모든 행성을 터널로 연결하는데 필요한 최소 비용 -> 최소신장트리
# x, y, z축에 대하여 정렬 후 각각 n-1개의 간선만 고려
# 크루스칼 알고리즘

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
        
n = int(input())
parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

e = []
result = 0

x = []
y = []
z = []

for i in range(1, n+1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))
    
x.sort()
y.sort()
z.sort()

# 인접한 노드들로부터 간선 정보를 추출하여 정리
for i in range(n-1):
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    e.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    e.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1])) 
    e.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))
    
e.sort()

for edge in e:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        
print(result)