# 행 1~8, 열 a~h
# 상하좌우 문제
# 완전탐색
# ord() -> 문자를 유니코드 정수로, chr() -> 숫자를 해당 문자로

m = input()
row, col = int(m[1]), int(ord(m[0]))

# 움질일 수 있는 방향 모두
l = [[-2, -1], [-2, 1], [-1, -2], [1, -2], [2, -1], [2, 1], [-1, 2], [1, 2]]

result = 0

for i in range(8):
    new_row = row + l[i][1]
    new_col = col + l[i][0]
    if (new_row < 1) or (new_row > 8) or (new_col < int(ord('a'))) or (new_col > int(ord('h'))):
        continue
    else:
        result += 1

print(result)