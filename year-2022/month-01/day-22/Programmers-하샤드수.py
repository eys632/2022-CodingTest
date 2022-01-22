"""

Code-1 설명
    - 자연수 x를 문자열로 만들어 for 문에 넣어주고 글자수만큼 for문을 돌렸습니다.
    - 글자 각각을 a에 넣어주고 그것을 정수로 변환하여 리스트에 각각 넣어주었습니다.
    - 그리고 만들어진 리스트의 합을 구해 x % 합이 == 0 이면 True를 반환하였습니다.


Code-2 설명
    - get은 dictionary 함수로 True면 True False면 False를 변환한다.

"""


# Code-1
def solution(x):
    if x % sum([int(a) for a in str(x)]) == 0:
        answer = True
    else:
        answer = False
    return answer


# Code-2
def solution(x):
    {x % sum([int(a) for a in str(x)]) == 0: True}.get(True, False)