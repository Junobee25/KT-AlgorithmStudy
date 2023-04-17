# n*m 크기의 얼음 틀
# 0 : 구멍이 뚫려 있는 부분, 1 : 칸막이가 존재하는 부분

# dfs : 한 지점에서 구멍이 뚫려 있는 부분으로 계속 들어가면서 확인
n, m = map(int, input().split())
ice = []
for i in range(n):
    ice.append(list(map(int, input())))

icecream = 0

#상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 특정 지점 방문 후 연결된 구멍이 뚫려 있는(0인) 노드 방문
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m: # 범위 벗어날 경우 
        return False
    if ice[x][y] == 0:
        ice[x][y] = 1 # 방문 처리
        # 특정 노드의 상하좌우 확인
        for i in range(4):
            dfs(x+dx[i], y+dy[i])
        # dfs(x, y+1)
        # dfs(x, y-1)
        # dfs(x-1, y)
        # dfs(x+1, y)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            icecream += 1
            
print(icecream)