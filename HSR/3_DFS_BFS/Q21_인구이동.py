# n*n 크기의 땅
# 인구차이가 l이상 r이하라면 연합

from collections import deque

n, l, r = map(int, input().split())
people = []
for _ in range(n):
    people.append(list(map(int, input().split())))
    
# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

result = 0

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
    united = []
    united.append((x, y))
    queue = deque()
    queue.append((x, y))
    union[x][y] = index
    summary = people[x][y]
    count = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and union[nx][ny] == -1:
                if l <= abs(people[nx][ny] - people[x][y]) <= r:
                    queue.append((nx, ny))
                    union[nx][ny] = index
                    summary += people[nx][ny]
                    count += 1
                    united.append((nx, ny))
                    
    for i, j in united:
        people[i][j] = summary // count
    return count

total_count = 0

while True:
    union = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    if index == n*n:
        break
    total_count += 1
    
print(total_count)