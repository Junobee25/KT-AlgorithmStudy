# 내림차순으로 정렬

n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
    
num.sort(reverse=True)
# result = sorted(num, reversed=True)
# sorted는 새로운 리스트를 반환, sort는 그 리스트를 정렬하고 None을 반환

for i in num:
    print(i, end=' ')