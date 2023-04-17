# 내 풀이
n = input()
# ord : 문자의 유니코드 정수로 반환
col = ord(n[0]) - ord('a')
row = int(n[1]) - 1
result = 0
board_size = 8

moves = []
for dx, dy in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
    new_col = col + dx
    new_row = row + dy
    if 0 <= new_col < board_size and 0 <= new_row < board_size:
        result += 1
print(result)