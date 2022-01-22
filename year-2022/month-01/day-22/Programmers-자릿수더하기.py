"""

설명
    - n을 각각의 자릿수를 리스트에 넣어주고 sum을 이용하여 더해주었습니다.

"""


# Code
def solution(n):
    return sum([int(a) for a in str(n)])
