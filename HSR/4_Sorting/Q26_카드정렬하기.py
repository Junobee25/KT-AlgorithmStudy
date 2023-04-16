# N개의 숫자카드 묶음의 각각의 크기가 주어질 때,
# 최소한 몇 번의 비교가 필요한지
# 작은 것끼리 묶어서 비교하기
# 우선순위 큐 -> 힙

import heapq

n = int(input())
card = []
for i in range(n):
    data = int(input())
    heapq.heappush(card, data)
    
result = 0

# 힙에 원소가 1개 남을 때까지
while len(card) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(card)
    two = heapq.heappop(card)
    # 카드 묶음을 합쳐서 다시 넣기
    sum_card = one + two
    result += sum_card
    heapq.heappush(card, sum_card)
    
print(result)
