# 단순 구현 문제
# 4방향 벡터사용 하면서 위치 옮기기
n = int(input())
let_go = list(input())
result = [1,1]
matrix = [[0]*(n+1) for _ in range(n+1)]

# 좌표평면 내의 좌표인지 확인하는 함수
def check(result):
    if 1<=result[0]<n+1 and 1<=result[1]<n+1:
        return True
    else:
        return False
# 선형리스트
for i in let_go:
    if i == 'R':
        result[1] += 1
        if check(result):
            continue
        else:
            result[1] -= 1
    if i == 'L':
        result[1] += -1
        if check(result):
            continue
        else:
            result[1] -= 1
    if i == 'U':
        result[0] += -1
        if check(result):
            continue
        else:
            result[0] += 1
    if i == 'D':
        result[0] += 1
        if check(result):
            continue
        else:
            result[0] -= 1
print(result[0],result[1])