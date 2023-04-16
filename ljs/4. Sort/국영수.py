# 국영수
# https://www.acmicpc.net/problem/10825

n = int(input())
result = []
for i in range(n):
    name, k, e, m =  input().split()
    result.append((name, int(k), int(e), int(m)))

result = sorted(result, key = lambda x: (-x[1], x[2], -x[3], x[0]))

for element in result:
    print(element[0])