S = input()

s = [] # 문자열만 담을 리스트
n = 0 # 숫자를 더할 변수

# 0~9 (ord(9) == 49), ord(A) == 65
# isalpha() -> 알파벳인지 확인
# isdigit() -> 숫자인지 판단 (문자열이 숫자 형태인지)
# isdecimal()  -> 숫자인지 판단 (int로 변환할 수 있는지)
for i in range(len(S)):
    if int(ord(S[i])) < int(ord('A')):
        n += int(S[i])
    else:
        s.append(S[i])

s.sort()
result = ''
for i in s:
    result += i
    
result = result +  str(n)
print(result)