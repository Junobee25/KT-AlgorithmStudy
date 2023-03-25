# 시뮬레이션

# 벽면의 크기 n, 설치 및 삭제 작업이 순서대로 담긴 build_frame
# 규칙 1. 기둥은 바닥 위에 있거나 보의 한쪽 끝부분 위에 있거나, 다른 기둥 위에 있어야 한다.
# 규칙 2. 보는 한쪽 끝부분이 기둥 위에 있거나, 또는 양쪽 끝부분이 다른 보와 동시에 연결 되어야 한다.

# build_fram 원소 [x, y, a, b]
# x, y -> 설치 및 삭제할 곳의 좌표
# a -> 0: 기둥, 1: 보
# b -> 0: 삭제 1: 설치

# return [x, y, a]
# x, y -> 기둥, 보의 교차점 좌표
# a -> 0: 기둥, 1: 보

# 설치 및 삭제 연산을 할 때마다 규칙 확인하기

# 현재 설치된 구조물이 가능한 구조물인지 규칙 확인
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 기둥인 경우
            # 바닥위, 보의 한쪽 끝부분 위, 다른 기둥위 => 정상
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif stuff == 1: # 설치된 것이 보인 경우
            # 한쪽 끝부분이 기둥 위, 양쪽 끝부분이 다른 보와 동시에 연결 => 정상
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        
        if operate == 0: # 삭제하는 경우
            answer.remove([x, y, stuff]) 
            if not possible(answer): # 삭제 후 가능한지 확인
                answer.append([x, y, stuff]) # 불가능이면 다시 설치
        
        if operate == 1: #설치하는 경우
            answer.append([x, y, stuff])
            if not possible(answer): # 설치 후 가능한지 확인
                answer.remove([x, y, stuff]) # 불가능이면 다시 제거
                
    return sorted(answer)