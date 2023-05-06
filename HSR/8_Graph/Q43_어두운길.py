# n개의 집, m개의 도로
# 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액 출력
# 크루스칼 알고리즘

def  find_parent(parent, x):
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
        
n, m = map(int, input().split())
parent = [0] * (n)

for i in range(n):
    parent[i] = i
    
e = []
result = 0 # 최종 비용
first = 0 # 모든 비용을 담는 변수
    
for _ in range(m):
    x, y, z = map(int, input().split())
    e.append((z, x, y))
    
e.sort()

for edge in e:
    z, x, y = edge
    first += z
    
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += z
        
# 절약할 수 있는 최대 금액 출력
print(first - result)