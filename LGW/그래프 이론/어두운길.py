def find_par (parent,x ):
    if parent[x] != x:
        parent[x] = find_par(parent,parent[x])
    return parent

def union_par(parent,a,b):
    a = find_par(parent,b)
    b= find_par(parent,a)

    if a < b:
        parent[b] = a
    else :
        parent[a] =b
n,m = map(int, input().split())
parent= [0]*(1,n+1)
edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    x,y,z = map(int, input().split())
    edges.append(z,x,y)

edges.sort()
total = 0

for edge in edges:
    cost, a, b, = edge
    total += cost

    if find_par(parent,a) != find_par(parent,b):
        union_par(parent,a,b)
print(total-result)