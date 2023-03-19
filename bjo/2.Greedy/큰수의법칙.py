# 왜 그리디 알고리즘으로?
# -> 최대값을 구하기 위해선 현재 상황에서 가장 큰 수를 택해야하기 때문.

# 배열의 크기, 숫자가 더해지는 횟수, 중복
n,m,k = map(int,input().split())
num_arr = list(map(int,input().split()))

# 정렬
num_arr.sort(reverse=True)

## Acess 1.
# 숫자가 모두 다를 경우
# 중복되는 숫자가 있는 경우

## Acess 2.
# 굳이 케이스를 나눌 필요없이 최대숫자,최대숫자보다 한단계 작거나 아니면 최대 숫자와 같은 숫자를 더하기
cnt = 0 # 중복횟수
result = 0 # 누적합
flag = 0 # while문 반복 횟수 flag
while True:
    cnt += 1
    flag += 1
    if flag > m:
        break
    if cnt > k:
        result += num_arr[1] # 중복되는 숫자 포함 두번째로 큰수
        cnt = 0
    else:
        result += num_arr[0] # 제일 큰수
print(result)
        
        
        