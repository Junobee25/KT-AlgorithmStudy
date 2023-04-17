# 문제 이해
# 먹어야 할 N 개의 음식의 시간이 주어짐
# 1번 부터 먹기
# 마지막 음식 먹고 다시 1번 부터
# 1초 섭취 후 다음 음식 먹기 남아있는 것들 중 가장 가까운 음식 부터
# K초 후에 몇 번 음식 부터 다시 먹어야 하는지

# 3, 1, 2

# 접근
# while이 한번 돌면 리스트의 길이만큼 시간 ++
# while문안에 for문을 돌면서 요소 -= 1
# 0이 되면 -1 하지 않고 시간도 줄지 않는다
# 만약에 시간이 k초가 지나고 -=1 된 요소의 다음 인덱스가 정답

## 결과 => 시간초과 O(N^2) => 200,000 * 200,000 => 40,000,000,000

k = int(input())
food_times = list(map(int,input().split()))

def solution(food_times, k):
    # 시간 count
    s = 0
    idx = 0
    answer = 0
    # 회전은 while문 + for문
    while True:
        for i in range(len(food_times)):      
            # 다 먹지 않았을 때만 먹기
            if food_times[i] != 0:
                # 먹으면 시간 줄기
                food_times[i] -= 1
                # 시간 경과 count
                s += 1
            print(food_times,s,"초")
            # 모두 다 먹으면 -1 return
            if all(t==0 for t in food_times):
                return -1
            # k초에서 네트워크 장애 발생          
            if s == k :
                idx = i # idx flag 저장
                break
        if s==k:
            break
    print(idx,"먹는거 중단 시점")
    
    # 네트워크 장애 발생 시 idx가 마지막 요소 이면
    if idx == len(food_times) - 1:
        # 장애복구 후 처음 요소부터 모두 탐색
        for i in range(len(food_times)):
            if food_times[i] != 0:
                answer = i
                break
    else:     
        # 인덱스가 마지막 요소가 아니면 오른쪽 부터 탐색      
        for i in range(idx+1,len(food_times)):
            if food_times[i] != 0:
                answer = i
                return answer + 1
        # 오른쪽 탐색 후 없으면 처음부터 돌아가서 찾기(왼쪽에 있음)
        for i in range(len(food_times)):
            if food_times[i] != 0:
                answer = i
                break
                          
    return answer + 1
print("몇번 째 음식을 먹어야 하니",solution(food_times,k))