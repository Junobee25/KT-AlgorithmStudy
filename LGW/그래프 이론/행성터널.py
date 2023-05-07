def find_par(parent,x):
    if parent[x] != x:
        parent[x] = find_par(parent,parent[x])
    return parent

def union_par(parent,a,b):
    a = find_par(parent,a)
    b = find_par(parent,b)

    if a < b:
        parent[b] = a
    else :
        parent[a] =b
n = int(input())
parent = [0] * (1,n+1)

edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i

x =[]
y =[]
z = []

for i in range(1, n+1):
    data = list(map(int,input().split()))
    x.append(data[0],i)
    y.append(data[1],i)
    z.append(data[2],i)
x.sort()
y.sort()
z.sort()

for i in range(n-1):
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i+1][1]))

edges.sort()

for edge in edges:
    cost,a,b = edge
    if find_par(parent,a,b):
        union_par(parent,a,b)
        result += cost
print(result)