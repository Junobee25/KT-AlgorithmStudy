n = int(input('개수입력:'))
data = list(map(int,input('리스트입력:').split()))

data.sort()

target = 1
for i in data:
    if target < i:
        break
    target += i

print(target)

