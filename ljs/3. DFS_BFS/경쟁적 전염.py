# 경쟁적 전염
from collections import deque
turns=[[0,1],[0,-1],[1,0],[-1,0]]


n,k=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
s,X,Y=map(int,input().split())

virus=[[] for i in range(k)] 
for i in range(n):
    for j in range(n):
        if arr[i][j]!=0:
            virus[arr[i][j]-1].append([i,j])
            
for time in range(s):
    tmp=[[] for i in range(k)]
    for types in range(k):
        for v in virus[types]:
            for turn in turns:
                x,y=v[0]+turn[0],v[1]+turn[1]
                if x<0 or y<0 or x==n or y==n:
                    continue
                if arr[x][y]==0:
                    arr[x][y]=arr[v[0]][v[1]]
                    tmp[types].append([x,y])
    virus=tmp
print(arr[X-1][Y-1])