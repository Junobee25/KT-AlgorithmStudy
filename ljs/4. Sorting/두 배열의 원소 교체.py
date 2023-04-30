# 두 배열의 원소 교체
n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a_s = sorted(a)[k:]
b_s = sorted(b, reverse = True)[:k]
result = a_s + b_s

sum = 0
for i in result:
    sum += i
print(sum)