# 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
# N : 전체 스테이지의 개수
# stages : 사용자가 현재 멈춰 있는 스테이지의 번호
# 실패율이 높은 스테이지부터 내림차순으로 출력

def solution(N, stages):
    answer = []
    people = len(stages) # 게임 사용자 수
    
    for i in range(1, N+1):
        count = stages.count(i) # 각 스테이지별 머물러 있는 사람 수
        
        # 실패율 계산
        if people == 0:
            fail = 0
        else:
            fail = count / people
        
        # 스테이지번호, 실패율 삽입    
        answer.append((i, fail))
        people -= count
        
    answer = sorted(answer, key=lambda x: x[1], reverse=True) # 내림차순 정렬
    answer = [i[0] for i in answer]
        
    return answer

    # fail = [[0] * 2 for _ in range(N+1)]
    # # 스테이지 멈춰 있는 사용자 수
    # for i in stages:
    #     fail[i][0] += 1
    
    # people = len(stages)
    # for i in range(1, N+1):
    #     # 스테이지별 실패율 계산
    #     if people == 0:
    #         break
    #     fail[i][1] = fail[i][0]/people
    #     people = people - fail[i][0]
        
    # result = sorted(fail, reverse=True, key=lambda x: x[1] )
    # for i in range(N):
    #     answer.append(result[i][0])