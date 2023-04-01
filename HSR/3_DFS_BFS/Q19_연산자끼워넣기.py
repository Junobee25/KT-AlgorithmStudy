n = int(input()) # 수의 개수
num = list(map(int, input().split())) # 수
cal = list(map(int, input().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈의 개수

min_num = 999999
max_num = -1

def dfs(i, now):
    global min_num, max_num, cal
    if i == n:
        min_num = min(min_num, now)
        max_num = max(max_num, now)
    else:
        if cal[0]>0:
            cal[0] -= 1
            dfs(i+1, now + num[i])
            cal[0] += 1
        
        if cal[1]>0:
            cal[1] -= 1
            dfs(i+1, now - num[i])
            cal[1] += 1
            
        if cal[2]>0:
            cal[2] -= 1
            dfs(i+1, now * num[i])
            cal[2] += 1
            
        if cal[3]>0:
            cal[3] -= 1
            dfs(i+1, now // num[i])
            cal[3] += 1

dfs(1, num[0])
print(max_num)
print(min_num)