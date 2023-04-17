def solution(food_times, k):   
    foods = []
    n = len(food_times)
    for i in range(n):
        # 먹는 시간과, 위치
        foods.append((food_times[i], i + 1))
    # 작은 값부터 비교를 하겠다.
    foods.sort()
    s = 0 # 갱신 해야될 시간
    for i, food in enumerate(foods):
        # 초기값은 최소 값
        diff = food[0] -s
        if diff != 0:
            spend = diff * n
            if spend <= k :
                # 시간을 한번에 빼기
                k -= spend
                s = food[0]
            else:
                k %= n
                # sublist = sorted(foods[i:], key = itemgetter(1))
                sublist = sorted(foods[i:], key = lambda x : x[1])
                return sublist[k][1]
        n -= 1 
    return -1

# 배운 점
# 1초가 지났을 때 남아있는 음식을 하나하나 확인하는 것이 아니라
# 1초가 지났을 때 먹을 수 있는 음식을 (최소값 기준으로) 한번에 처리해 줌으로써 diff * n
# 시간복잡도를 줄일 수 있음
# k초가 지난 후 남아있는 음식들 중에서 나머지를 통해 인덱스를 구하고
# lambda 정렬 후 return
# 뭉탱이로 날린다. 그래서 시간복잡도가 줄어든다!

