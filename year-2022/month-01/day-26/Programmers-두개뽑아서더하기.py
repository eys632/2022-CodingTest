"""

설명
    - 같은 원소값이 있으면 pass 하라고 했는데 오류가 떴다 .
      그 이유는 s 리스트 안에 같은 원소가 존재할 수 있기 떄문이다.

"""


# Code
def solution(s):
    answer = []
    for i in range(len(s)):
        for j in range(len(s)):
            if i == j:
                pass
            else:
                answer.append(s[i] + s[j])
    return sorted(list(set(answer)))


