#여행 계획
# 서로소 집합 알고리즘
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

n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(n):
    value = list(map(int, input().split()))
    for j in range(n):
        if value[i] == 1:
            union_parent(parent, i+1, j+1)
            
plane = list(map(int, input().split()))

def possible(first):
    for i in plane:
        if i != find_parent(parent, i):
            return "NO"
    return "YES"

print(possible(find_parent(parent, plane[0])))
    