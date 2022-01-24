"""

설명
    - 문자열의 길이가 4또는 6일때 그 문자열이 숫자만있는지 판단


함수
    문자열.isnumeric()
        - 숫자로만 이루어져있다면 True, 문자열이 하나라도 있다면 False

"""


# Code
def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isnumeric()
    return False
