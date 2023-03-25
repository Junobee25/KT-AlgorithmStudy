n = input()

l = len(n)
# 길이의 절반으로 왼쪽, 오른쪽 나누기
left = n[0:l//2]
right = n[l//2:]

left_sum, right_sum = 0, 0
for i in range(l//2):
    left_sum += int(left[i])
    right_sum += int(right[i])    
    
if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')