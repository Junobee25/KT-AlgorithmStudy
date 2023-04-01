# 연구소 크기 n*m
# 새로 세울 수 있는 벽의 개수 3개
# 0: 빈칸, 1: 벽, 2: 바이러스
# 벽을 3개 세운 후, 바이러스가 퍼지고 남은 안전영역 계산

n, m = map(int, input().split())
lab = [] # 연구소 상태
temp = [[0]*m for _ in range(n)] # 벽 설치 후

for _ in range(n):
    lab.append(list(map(int, input().split())))

# 상, 하, 좌, 우 (바이러스가 상하좌우로 퍼짐)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

result = 0

# 사방으로 퍼지는 바이러스 구현 => DFS
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 연구소 영역
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)
           
# 안전 영역 계산                
def safe():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 벽을 설치하면서 매번 안전 영역 크기 계산
def dfs(count):
    global result
    # 벽이 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = lab[i][j]
    
        # 바이러스의 위치 정보, 바이러스 전파            
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
                    
        # 안전 영역의 최댓값 계산
        result = max(result, safe())
        return
    
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                count += 1
                dfs(count)
                lab[i][j] = 0
                count -= 1
                
dfs(0)
print(result)