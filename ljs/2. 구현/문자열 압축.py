
#  문자열 압축
def solution(s):
    m_len = len(s)
    # 늘려가면서 확인
    for i in range(1, len(s) // 2 + 1):
        new_s = ''
        cnt = 1
        # i만큼의 간격으로 확인
        for j in range(0, len(s), i):
            if s[j:j+i] == s[j+i:j+2*i]:
                cnt += 1
            else:
                if cnt != 1:
                    new_s += str(cnt)
                new_s += s[j:j+i]
                cnt = 1

        min_len = min(m_len, len(new_s))

    return min_len