# -/-사이에있는 문자는 더해주기
# 그리고 모든 리스트 빼주기
num_arr = input().split('-')
num = []
for i in num_arr:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1,len(num)):
    n -= num[i]
print(n)