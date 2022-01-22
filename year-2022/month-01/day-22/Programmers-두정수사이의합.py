"""

설명
    - if문을 사용하지 않았는데 사용한 것 처럼 됐다.
    - a<b이면 range(a,b+1)을 하여 i 값을 answer에 넣어주었습니다.
    - a>b이면 range(b,a+1)을 하여 i 값을 answer에 넣어주었습니다.
    - a=b이면 둘다 상관없으니 둘 중 하나에서 실행 되었습니다.

"""


# Code
def solution(a, b):
    answer = 0
    for i in range(a, b + 1): answer += i
    for i in range(b, a + 1): answer += i
    return answer
