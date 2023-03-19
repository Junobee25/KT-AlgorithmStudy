# 전형적인 시뮬레이션 구현 문제 (50분)
n,m = map(int,input().split())
cy,cx,direc = map(int,input().split())
direction = [0,1,2,3] # 북/동/남/서
game = []
visited = [[False]*m for _ in range(n)]

for _ in range(n):
    game.append(list(map(int,input().split())))
    
dy = [-1,0,1,0] # 북 서 남 동 
dx = [0,-1,0,1]
vi_cnt = 0
while True:
    flag = 0
    if direc == 0: # 북쪽인 경우
        cy += dy[1]
        cx += dx[1]
        if 0<=cy<n and 0<=cx<m and visited[cy][cx] == False and game[cy][cx] != 1:
            visited[cy][cx] = True
            vi_cnt += 1
        else:
            cy -= dy[1]
            cx -= dx[1]
        direc = 3 # 서쪽으로 방향 전환   
    if direc == 1: # 동쪽인 경우
        cy += dy[0]
        cx += dx[0]
        if 0<=cy<n and 0<=cx<m and visited[cy][cx] == False and game[cy][cx] != 1:
            visited[cy][cx] = True
            vi_cnt += 1
        else:
            cy -= dy[0]
            cx -= dx[0]
        direc = 0 # 북쪽으로 방향 전환    
    if direc == 2: # 남쪽인 경우
        cy += dy[3]
        cx += dx[3]
        if 0<=cy<n and 0<=cx<m and visited[cy][cx] == False and game[cy][cx] != 1:
            visited[cy][cx] = True
            vi_cnt += 1
        else:
            cy -= dy[3]
            cx -= dx[3]
        direc = 1 # 동쪽으로 방향 전환    
    if direc == 3: # 서쪽인 경우
        cy += dy[2]
        cx += dx[2]
        if 0<=cy<n and 0<=cx<m and visited[cy][cx] == False and game[cy][cx] != 1:
            visited[cy][cx] = True
            vi_cnt +=1
        else:
            cy -= dy[2]
            cx -= dx[2]
        direc = 2 # 남쪽으로 방향 전환
    # 4방향 탐색 3번 조건 검사
    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]
        if 0<=ny<n and 0<=nx<m and visited[ny][nx] == False and game[ny][nx] != 1:
            continue
        else:
            flag += 1
    if flag == 4:
        if direc == 0: # 북쪽이면 남쪽으로 이동
            cy += dy[2]
            cx += dx[2]
            if game[cy][cx] == 1:
                break
        if direc == 1: # 동쪽이면 서쪽으로 이동
            cy += dy[1]
            cx += dx[1]
            if game[cy][cx] == 1:
                break
        if direc == 2: # 남쪽이면 북쪽으로 이동
            cy += dy[0]
            cx += dx[0]
            if game[cy][cx] == 1:
                break
        if direc == 3: # 서쪽이면 동쪽으로 이동
            cy += dy[3]
            cx += dx[3]
            if game[cy][cx] == 1:
                break
print(vi_cnt+1)