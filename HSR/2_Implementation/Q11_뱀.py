# 시뮬레이션
n = int(input()) # n*n 보드
k = int(input()) # 사과 개수
data = [[0]*(n+1) for _ in range(n+1)] # 맵
info = [] # 방향 회전 정보

# 사과가 있는 곳 표시
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1
    
# 방향 회전 정보
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))
    
# 첫 시작 오른쪽 (동 남 서 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1)%4
    else:
        direction = (direction + 1)%4
        
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2 # 맵에서 뱀이 존재하는 위치
    direction = 0 # 처음 동쪽
    time = 0 # 지난 시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리 정보)
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 이동했는데 맵 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0) # 처음있던 위치
                data[px][py] = 0 # 제거 => 꼬리 제거
                
            # 사과가 있다면 이동 후 그대로
            if data[nx][ny] == 1:
                data[nx][ny] == 1
                data[nx][ny] = 2
                q.append((nx, ny))
        # 이동했는데 벽이나 몸통에 부딪힌 경우
        else:
            time += 1
            break
        
        x, y = nx, ny # 다음 위치로 머리 이동
        time += 1
        if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
        return time
    
    print(simulate())
                    