# Acess 1
# 갈수있는 최대 경우의수 8 가지
n = input()
check_night = [(-2,1),(-2,-1),(-1,2),(1,2),(2,1),(2,-1),(-1,2),(-1,-2)]
name = [0,'a','b','c','d','e','f','g','h']
matrix = [[name[i]+str(k) for i in range(1,9)] for k in range(1,9)]
result = []
for i in range(8):
    for j in range(8):
        if matrix[i][j] == n:
            result = [i+1,j+1]
cnt = 0
# 갈 수있는 위치면 +=1
for i,j in check_night:
    y,x = result[0]+i,result[1]+j
    if 1<=y<9 and 1<=x<9:
        cnt += 1
print(cnt)