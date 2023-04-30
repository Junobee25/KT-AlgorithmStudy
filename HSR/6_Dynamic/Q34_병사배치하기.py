# n명의 병사, 전투력이 높은순으로 배치
# 남아 있는 병사의 수가 최대가 되도록 하기 위해 열외시켜야 하는 병사의 수

# 가장 긴 증가하는 부분 수열 참고 - > 가장 긴 감소하는 부분 수열
# D[i] = array[i]
# D[i] = max(D[i], D[j]+1) if array[j] < array[i]

n = int(input())
array = list(map(int, input().split()))

array.reverse() # 내림차순

d = [1]*n

# 최장 길이 출력
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            d[i] = max(d[i], d[j]+1) #뒤에 오는 것이 작을 경우, 횟수 증가
            
print(n - max(d)) # 열외 시킬 병사 수