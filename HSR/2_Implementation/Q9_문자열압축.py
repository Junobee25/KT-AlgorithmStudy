# 완전 탐색
# 문자열 압축을 1부터 ~ n//2까지

def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)//2+1):
        m = ''
        p = s[0:i] # 문자열 압축 단위
        count = 1
        
        for j in range(i, len(s), i): # 문자열 압축단위로 비교
            if p == s[j:j+i]: # 이전상태와 동일할 경우
                count += 1
            else: # 다를 경우
                if count >= 2:
                    m += str(count) + p
                else:
                    m += p
                p = s[j:j+i] # 다음 압축단위
                count = 1
        # 남아있는 문자열 처리
        if count >= 2:
            m += str(count) + p
        else:
            m += p
            
        # 만들때마다 문자열 길이 비교   
        answer = min(answer, len(m)) 
                        
    return answer