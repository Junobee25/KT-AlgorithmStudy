# 자물쇠 : n*n 크기의 정사각 격자 형태
# 열쇠 : m*m 크기의 정사각 격자 형태
# 0은 홈 부분, 1은 돌기 부분 -> 돌기부분과 홈부분이 완벽히 일치해야 됨.
# 완전탐색
# 자물쇠 크기 늘리기 -> 열쇠 90도씩 회전하며 크기 맞추기

# 2차원 리스트 90도 회전 함수
def rotate_90_degree(a):
    n = len(a) # 행 길이
    m = len(a[0]) # 열 길이
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result
    
# 자물쇠가 1이 되었는지 확인
def check(new_lock):
    lock_length = len(new_lock)//3 # 원래 크기
    # new_lock의 크기가 3배 이므로, 기존의 자물쇠는 정 가운데에 있음.
    # 기존 자물쇠를 확인하기 위해서
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
            
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠 크기 기존의 3배로
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    # 중앙에 기존 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    # 4가지 방향으로 회전
    for rotation in range(4):
        key = rotate_90_degree(key)
        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠에 열쇠 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                        
                if check(new_lock) == True:
                    return True
                
                # 자물쇠에서 열쇠 빼기
                for i in range(m):
                    for  j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    
    return False