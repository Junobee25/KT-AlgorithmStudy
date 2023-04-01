#괄호변환
def get_uv(p):
    a = 0
    for i, e in enumerate(p):
        if e == "(":
            a += 1
        else:
            a -= 1
        if a == 0:
            return p[:i+1], p[i+1:]
        
def is_u_right(u):
    stack = []
    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    if p == "": return p
    u, v = get_uv(p)
    if is_u_right(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        for p in u[1:len(u)-1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('
        return answer