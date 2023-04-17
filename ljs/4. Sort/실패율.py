# 실패율
def solution(N, stages):
    num = [0] * (N+2)                                                
    res = []

    for i in stages: 
        num[i] += 1 # 각 스테이지 번호,해당 스테이지 번호에 인덱스의 값 1씩 증가

    for j in range(1, len(num)-1):
        if num[j] != 0:
            fail = num[j] / sum(num[j:])
            res.append((j,fail)) # 스테이지 번호, 실패율
        else: res.append((j,0))
        
    res.sort(key = lambda x:(-x[1],x[0])) # x[1]을 내림차순, x[0]을 오름차순

    answer = []                                            
    for k in res:
        answer.append(k[0])
    return answer