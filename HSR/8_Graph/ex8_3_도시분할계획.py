# 2개의 분리된 마을간의 경로 x, 길의 유지비의 합을 최소
# 최소 신장트리에서 가장 큰 간선 제거하기
# 크루스칼 알고리즘
 
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 집과 길의 개수
n, m = map(int, input().split())
parent = [0] * (n+1)

# 간선을 담을 리스트와 최종 비용
e = []
result = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    e.append((c, a, b))
    
e.sort() # 비용순으로 정렬

max_cost = 0 # 가장 높은 비용 저장

for edge in e:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c
        max_cost = c

print(result - max_cost)