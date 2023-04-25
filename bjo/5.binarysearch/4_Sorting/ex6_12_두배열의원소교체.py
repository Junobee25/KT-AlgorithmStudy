# a와 b배열의 원소를 k번 바꿔서 a의 합이 크도록
# a의 작은 수와 b의 큰 수를 교환

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]>b[i]: # a의 원소가 b의 원소보다 작을 경우에만 교환
        break
    else:
        a[i], b[i] = b[i], a[i]

sum = 0
for i in a:
    sum += i

print(sum)