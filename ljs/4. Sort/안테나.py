# 안테나
# https://www.acmicpc.net/submit/18310/58916624
n = int(input())
loca = list(map(int, input().split()))
loca = sorted(loca)

lo_len = len(loca)//2
arr = []
for i in loca:
    arr.append(abs(i - loca[lo_len]))

sum = 0
sum2 = 0
for i in range(n):
    sum += arr[i]
    sum2 += arr[i]
    
if sum >= sum2:
    print(loca[lo_len-1])
else:
    print(loca[lo_len])