N, M, K = map(int, input().split())
num = list(map(int, input().split()))

num.sort()

count = 0
sum_count = 0
sum_num = 0

# 큰 수 K번, 그 다음 수 1번 반복
while sum_count != M:
    if count < K:
        sum_num += num[N-1]
        count += 1
    else:
        sum_num += num[N-2]
        count = 0
        
    sum_count += 1
        
print(sum_num)