s = input()

count_zero = 0 # 0으로 바꿀 경우
count_one = 0 # 1로 바꿀 경우

if s[0] == '1':
    count_zero += 1
else:
    count_one += 1
    
for i in range(len(s)-1):
    if (s[i] == '0') & (s[i+1] == '1'):
        count_zero += 1
    elif (s[i] == '1') & (s[i+1] == '0'):
        count_one += 1
        
    # if s[i] != s[i+1]:
    #     if s[i+1] == '1':
    #         count_zero += 1
    #     else:
    #         count_one += 1


print(min(count_zero, count_one))