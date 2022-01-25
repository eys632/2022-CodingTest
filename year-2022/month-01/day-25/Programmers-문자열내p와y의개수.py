"""

설명
    - 문자열의 대소문자를 구분해주는 것 보다 문자열 전체를 소문자로 만들어 비교하는게 좋다고 생각했습니다.
    - 문자열에 특정 문자가 있는지 count를 사용해서 비교를 해주었습니다.

"""


# Code
def solution(s):
    s = s.lower()
    if s.count("p") == s.count("y"):
        return True
    else:
        return False
