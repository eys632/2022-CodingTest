"""

설명
    - range의 특징을 이용하여 x부터 시작하여 x씩 증가, 숫자 n개 지니게 하였습니다.
    - 그리고 i를 append 시켜주었습니다.
    - x = 0 이 경우는 0을 리스트에 n번 append 시켜주었습니다.


함수
    range
        - range(시작,끝,증감크기)

"""


# Code
def solution(x, n):
    answer = []
    if x != 0:
        for i in range(x, x * n + x, x):
            answer.append(i)
    else:
        for i in range(n):
            answer.append(0)
    return answer
