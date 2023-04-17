# 균형잡힌 괄호 문자열 : '('와 ')'의 개수가 같은 경우
# 올바른 괄호 문자열 : 괄호의 개수와 짝도 모두 맞을 경우

# 균형잡힌 괄호 문자열 인덱스 반환
def balance(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        
        if count == 0:
            return i
    


# 올바른 괄호 문자열인지
def perpect(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
        
    return True

def solution(p):
    answer = ''
    # 문자열이 빈 문자열일 경우, 빈 문자열 반환
    if p == '':
        return ''
    
    idx = balance(p)
    u = p[:idx+1]
    v = p[idx+1:]
    
    # 올바른 괄호 문자열인지 확인
    if perpect(u):
        answer = u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
            
    return answer