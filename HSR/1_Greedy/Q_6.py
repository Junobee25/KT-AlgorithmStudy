food_times = list(map(int, input().split())) # 음식 배열
k = int(input()) # 중단된 시간

def solution(food_times, k):
    answer = 0
    
    n = len(food_times)
    i = 0
    
    while k!=0:
        if i == n:
            i = 0
        
        if food_times[i] > 0:
            food_times[i] -= 1
            k -= 1
            i += 1
        else:
            i += 1
            
    check = 0 # 먹을 음식이 없는지 확인
    for i in range(n):
        if food_times[i] == 0:
            check = -1
        else:
            check = 0
            break
            
    if check == -1:
        return -1
    else:
        if i == n:
            answer = 1
        else:        
            answer = i+1
    
    return answer

print(solution(food_times, k))