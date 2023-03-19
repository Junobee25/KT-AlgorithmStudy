# 문제이해
# 모든 숫자를 같게 만들기 위한 뒤집기 행동의 최소 횟수

# 접근
# 연속되어 있는 숫자의 집합이 작은 집합을 뒤집기

string = input()

zero_set = 0 # 0으로 구성된 집합의 갯수
one_set = 0 # 1로 구성된 집합의 갯수

start = string[0]

if all(k=='0' for k in string):
    print(0)
    exit()
if all(k=='1' for k in string):
    print(0)
    exit()   
# 집합이 무조건 하나 존재하므로 집합 개수 + 1
if start[0] == '0':
    zero_set += 1
else:
    one_set += 1

for i in range(len(string)):
    if start != string[i] and string[i] == '1': # 기준요소와 달라지는 시점에 요소가 1이면
        one_set += 1 # 1의 집합 카운트
        start = string[i] # 기준요소 변경
    elif start != string[i] and string[i] == '0':
        zero_set += 1
        start = string[i]
print(min(one_set,zero_set)) # 집합의 갯수가 최소인 집합만 뒤집기