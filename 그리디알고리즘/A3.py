## 입력 조건 : 첫째 줄에 0과1로만 이루어진 문자열 S가 주어집니다. S의 길이는 100만보다 작습니다.
## 출력 조건 : 첫째 줄에 다솜이가 해야하는 행동의 최소 횟수를 출력합니다.
data = input('문자열 입력 :')
cnt0 = 0 #모두 0으로 바꾸는 경우
cnt1 = 0 #모두 1으로 바꾸는 경우

if data[0] == '1':
    cnt0 += 1
else :
    cnt1 += 1

for i in range(len(data)-1): # 두번째 원소 부터
    if data[i] != data[i+1]: # 해당원소와 뒤의원소가 다르면
        if data[i+1] == '1': #
            cnt0 += 1
        else :
            cnt1 += 1

print(min(cnt0,cnt1))
00