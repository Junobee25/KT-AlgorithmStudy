from collections import deque ## deque는  앞, 뒤 양쪽 방향에서 엘리먼트(element)를 추가하거나 제거할 수 있다.

n,l,r = map(int,input().split())

grp = []
for _ in range(n):
    grp.append(list(map(int,input().split())))

#좌표별 이동 상, 하 , 좌 ,우
dx = [-1,0,1,0]
dy = [0,-1,0,1]

result = 0

def process(x,y,index):
    untied = []
    untied.append((x,y)) # 왜 괄호를 두번인지 모르겠음.

    q = deque()
    q.append((x,y))
    union[x][y] = index #현재 연합의 번호 할당
    summary = grp[x][y]
    cnt = 1 # 현재 연합의 국가 수

    while q:
        x,y= q.popleft()

        for i in range(4): #현재 위치에서 4가지 방향 확인
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx and 0<=ny and union[nx][ny]== -1:
                if l <= abs(grp[nx][ny] - grp[x][y]) <= r:
                    q.append((nx,ny))
                    union[nx][ny]= index
                    summary += grp[nx][ny]
                    cnt += 1
                    untied.append((nx,ny))

    for i,j in untied:
        grp[i][j] = summary//cnt
    return cnt
total_cnt = 0

while True:
    union = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i,j,index)
                index +=1

    if index == n*n:
        break
    total_cnt +=1
print(total_cnt)
