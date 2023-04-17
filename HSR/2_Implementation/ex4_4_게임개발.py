# 맵 크기 N*M, 0:육지, 1:바다
# 0-북, 1-동, 2-남, 3-서
# 시뮬레이션

n, m = map(int, input().split())
x, y, r = map(int, input().split())
game = []
for i in range(n):
    game.append(list(map(int, input().split())))

# 북(0, -1) 동(1, 0) 남(0, 1) 서(-1, 0)   
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 맵에서 방문한 곳은 바다(1)로 바꾼다. -> 가지 못하는 곳

result = 1
check = 0 # 1인지 체크
while True:
    game[x][y] = 1 # 현재 서있는 곳
    
    # 1. 왼쪽으로 회전
    if r == 0:
        r = 3
    else:
        r -= 1
    
    nx = x + dx[r]
    ny = y + dy[r]
    
    # 2. 가본 칸 존재 -> 왼쪽 방향으로 회전(1번에서 수행)
    if game[nx][ny] == 1:
        continue
    # 2. 안가본 칸 존재 -> 회전 후 전진
    else:
        x, y = nx, ny
        result += 1
    
    # 3. 네 방향 체크
    for i in range(4):
        if game[dx[i]][dy[i]] == 1:
            check = 1
        else:
            check = 0
            break
    
    if check == 1:
        nx = x - dx[r]
        ny = y - dy[r]
        if game[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        
print(result)

########## 다시풀기 ###########