# 백준에 괄호문제 => 올바른괄호인지?
# 스택 자료구조 백준문제 
def is_correct(str):
    left = 0 # '왼쪽'
    right = 0 # '오른쪽'
    for i in range(len(str)):
        if str[i] == '(':
            left += 1
        else:
            right += 1
        if right > left: # 올바르지 않은 괄호 문자열이되고
            return False # False
    return True


def remove_reverse(str):
    new_str = ''
    str = str[1:len(str)-1]
    for i in range(len(str)):
        if str[i] == '(':
            new_str += ')'
        else:
            new_str += '('
    return new_str


def solution(p): # 1.~2 
    if len(p) == 0:
        return p
    left = 0  #'('
    right = 0 #')'
    idx = 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right: # 균형잡인 문자열로 분리를 할건데 더이상 분리할 수 없다 => 처음으로 같아질때
            idx = i
            break
    u = p[:idx+1] #'왼쪽'
    v = p[idx+1:] #'오른쪽'

    if is_correct(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + remove_reverse(u)