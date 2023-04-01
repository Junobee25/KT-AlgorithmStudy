# LRUD
# 공간을 벗어나는 움직임 무시
 
n = int(input())
map = list(input().split())

x, y = 1, 1

for i in range(len(map)):
    if map[i] == 'L':
        y = y - 1
        if y == 0:
            y += 1
    elif map[i] == 'R':
        y = y + 1
        if y == NotImplemented:
            y -= 1
    elif map[i] == 'U':
        x = x - 1
        if x == 0:
            x += 1
    elif map[i] == 'D':
        x = x + 1
        if x == n:
            x -= 1

print(x ,y)

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move = ['L', 'R', 'U', 'D']

# for plan in map:
#     for i in (len(move)):
#         if plan == move[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
        
#         if nx<1 or ny<1 or nx>n or ny>n:
#             continue
#         x, y = nx, ny