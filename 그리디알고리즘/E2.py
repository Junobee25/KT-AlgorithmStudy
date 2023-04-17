## 큰수의 법칙

# 입력 조건 1. 첫째 줄에 N,M,k의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 입력 조건 2. 둘째줄에 N개 이하의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각가의 자연수는 1이상 10,000이하의 수로 주어진다.
# 입력 조건 3. 입력으로 주어지는 K는 항상 M보다 작거나 같다.

# 출력 조건 첫재 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

N,M,K = map(int, input('자연수 입력, 공백 구분').split())  #M= 더할 횟수 K 반복적으로 더해질수 있는 제한
data = list(map(int, input('N보다 작은수 입력').split()))

data.sort()
d1 = data[N-1]
d2 = data[N-2]

rls = 0

while True :
    for i in range(K) :
        if M<1:
            break
        rls += d1
        M -= 1
    if M== 0 :
        break
    rls += d2
    M-=1

print(rls)
