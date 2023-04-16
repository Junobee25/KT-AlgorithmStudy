# 부품찾기
n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

for i in b:
    if i in a:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')
