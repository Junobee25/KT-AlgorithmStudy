## 입력 조건 : 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어 집니다.(1<=S<=20)
## 출력 조건 : 춧째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.

s = input('숫자열을 입력해 주세요')
result = int(s[0])

for i in range(1,len(s)) :
    num = int(s[i])
    if num <= 1 or result<=1: #0혹은 1인경우 곱하기 보단 더하기 실행
        result += num
    else :
        result *= num

print(result)