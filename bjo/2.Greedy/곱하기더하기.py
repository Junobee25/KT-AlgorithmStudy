# 문제 이해
# 왼쪽부터 적절한 + or x 조합 연산을했을 때 만들 수 있는 가장 큰 수

# Access 
# 0과 1은 더하기 연산
# 0은 그냥 더하기
# (3+1) * 2 // 3 * (1 + 2)
# 나머지는 곱하기 연산을 한다.

number = list(input())

# total = 0

# for i in range(len(number)):
#     # total이 0 이면 더하기 연산
#     if total == 0:
#         total += int(number[i])
#     # total이 0이 아닐 때
#     else:
#         if number[i] == '0':
#             total += 0
#         if number[i] == '1' and (i != len(number) - 1):
#             if total >= int(number[i+1]):
#                 # 뒤에 숫자에 1을 더하는게 최대
#                 number[i+1] = str(int(number[i+1])+1)
#             else:
#                 # total 에 더하기
#                 total += 1
#         elif number[i] == '1' and (i == len(number) - 1):
#             total += 1
#         else:
#             total *= int(number[i])
# print(total)

result = int(number[0])

for i in range(1,len(number)):
    if int(number[i]) <= 1 or result <= 1:
        result += int(number[i])
    else:
        result *= int(number[i])
print(result)
